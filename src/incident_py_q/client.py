"""Incident IQ sync and async API clients with dynamic schema-driven SDK surfaces."""

from __future__ import annotations

import asyncio
import logging
import os
import time
from collections.abc import Mapping
from typing import Any, cast
from urllib.parse import urljoin

import httpx

from ._utils import render_path
from .apps import AppsNamespace, AsyncAppsNamespace
from .config import AuthMode, ClientConfig, build_authorization_value
from .exceptions import ConfigurationError
from .logging_utils import redact_headers
from .retry import compute_backoff_seconds, method_is_idempotent, should_retry_status
from .schema.loader import load_stoplight_documents
from .schema.registry import OperationSpec, SchemaRegistry, build_schema_registry
from .schema.validator import ResponseSchemaValidator
from .sdk.runtime import SDKArtifacts, build_sdk


class Client:
    """Synchronous Incident IQ API client.

    The client exposes a low-level request API and dynamically generated namespaces
    (for example `client.tickets`, `client.users`, `client.assets`) derived from
    bundled Swagger controller contracts.
    """

    def __init__(
        self,
        *,
        base_url: str | None = None,
        api_token: str | None = None,
        site_id: str | None = None,
        client_header: str = "ApiClient",
        auth_mode: str = "bearer",
        app_headers: Mapping[str, str] | None = None,
        timeout: float = 30.0,
        validate_responses: bool = True,
        max_retries: int = 2,
        backoff_base: float = 0.25,
        config: ClientConfig | None = None,
        registry: SchemaRegistry | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        if config is None:
            resolved_base_url = base_url or os.environ.get("INCIDENTIQ_BASE_URL")
            resolved_api_token = api_token or os.environ.get("INCIDENTIQ_API_TOKEN")
            if not resolved_base_url or not resolved_api_token:
                raise ConfigurationError(
                    "base_url and api_token are required (or set INCIDENTIQ_BASE_URL and "
                    "INCIDENTIQ_API_TOKEN)."
                )
            resolved_auth_mode = _normalize_auth_mode(auth_mode)
            config = ClientConfig(
                base_url=resolved_base_url.rstrip("/"),
                api_token=resolved_api_token,
                site_id=site_id,
                client_header=client_header,
                auth_mode=resolved_auth_mode,
                app_headers=_normalize_app_headers(app_headers),
                timeout=timeout,
                validate_responses=validate_responses,
                max_retries=max_retries,
                backoff_base=backoff_base,
            )

        self._config = config
        self._registry = registry or build_schema_registry(load_stoplight_documents())
        self._response_validator = ResponseSchemaValidator(self._registry)
        self._http = http_client or httpx.Client(timeout=config.timeout)
        self._logger = logging.getLogger("incident_py_q.client")

        self._sdk: SDKArtifacts = build_sdk(client=self, registry=self._registry, async_mode=False)
        for namespace_name, namespace_obj in self._sdk.namespaces.items():
            setattr(self, namespace_name, namespace_obj)
        self.apps = AppsNamespace(self)

    @classmethod
    def from_env(cls) -> Client:
        """Build a client from standard runtime environment variables."""
        return cls(config=ClientConfig.from_env(env=dict(os.environ)))

    @classmethod
    def from_test_env(cls) -> Client:
        """Build a client from integration test environment variables."""
        return cls(config=ClientConfig.from_env(env=dict(os.environ), test_mode=True))

    @property
    def config(self) -> ClientConfig:
        """Return immutable normalized runtime configuration."""
        return self._config

    def sdk_inventory(self) -> list[dict[str, str]]:
        """Return a stable inventory of generated SDK operations."""
        return list(self._sdk.inventory)

    def __getattr__(self, name: str) -> Any:
        namespace = self._sdk.namespaces.get(name)
        if namespace is not None:
            return namespace
        raise AttributeError(name)

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._http.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | list[Any] | None:
        """Send an HTTP request and validate successful JSON payloads by contract."""
        rendered_path = render_path(path, dict(path_params) if path_params else None)
        operation = self._registry.match_operation(method, rendered_path)
        return self._request_with_operation(
            method=method,
            rendered_path=rendered_path,
            operation=operation,
            params=dict(params) if params else None,
            json_body=json,
            headers=dict(headers) if headers else None,
            timeout=timeout,
        )

    def _request_from_operation(
        self,
        operation: OperationSpec,
        *,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> dict[str, Any] | list[Any] | None:
        rendered_path = render_path(operation.path_template, path_params)
        return self._request_with_operation(
            method=operation.method,
            rendered_path=rendered_path,
            operation=operation,
            params=params,
            json_body=json_body,
            headers=headers,
            timeout=timeout,
        )

    def _request_with_operation(
        self,
        *,
        method: str,
        rendered_path: str,
        operation: OperationSpec | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> dict[str, Any] | list[Any] | None:
        method_upper = method.upper()
        url = _build_url(self._config.base_url, rendered_path)
        merged_headers = _merge_headers(self._config, headers)
        request_timeout = timeout if timeout is not None else self._config.timeout
        can_retry = method_is_idempotent(method_upper)

        self._logger.debug(
            "incidentiq.request.start",
            extra={
                "method": method_upper,
                "path": rendered_path,
                "params": params or {},
                "headers": redact_headers(merged_headers),
            },
        )

        for attempt in range(self._config.max_retries + 1):
            try:
                response = self._http.request(
                    method_upper,
                    url,
                    params=params,
                    json=json_body,
                    headers=merged_headers,
                    timeout=request_timeout,
                )

                if (
                    should_retry_status(response.status_code)
                    and can_retry
                    and attempt < self._config.max_retries
                ):
                    delay = compute_backoff_seconds(attempt, self._config.backoff_base)
                    time.sleep(delay)
                    continue

                response.raise_for_status()
                payload = _decode_payload(response)
                if (
                    payload is not None
                    and self._config.validate_responses
                    and operation is not None
                ):
                    self._response_validator.validate(
                        operation,
                        status_code=response.status_code,
                        payload=payload,
                    )

                self._logger.debug(
                    "incidentiq.request.success",
                    extra={
                        "method": method_upper,
                        "path": rendered_path,
                        "status_code": response.status_code,
                    },
                )
                return payload

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code
                if should_retry_status(status_code) and can_retry and attempt < self._config.max_retries:
                    delay = compute_backoff_seconds(attempt, self._config.backoff_base)
                    time.sleep(delay)
                    continue
                self._logger.warning(
                    "incidentiq.request.http_error",
                    extra={
                        "method": method_upper,
                        "path": rendered_path,
                        "status_code": status_code,
                    },
                )
                raise
            except httpx.RequestError:
                if can_retry and attempt < self._config.max_retries:
                    delay = compute_backoff_seconds(attempt, self._config.backoff_base)
                    time.sleep(delay)
                    continue
                self._logger.warning(
                    "incidentiq.request.transport_error",
                    extra={"method": method_upper, "path": rendered_path},
                )
                raise

        # Loop always returns or raises before this point.
        raise RuntimeError("Request loop exhausted unexpectedly")


class AsyncClient:
    """Asynchronous Incident IQ API client with dynamic SDK parity."""

    def __init__(
        self,
        *,
        base_url: str | None = None,
        api_token: str | None = None,
        site_id: str | None = None,
        client_header: str = "ApiClient",
        auth_mode: str = "bearer",
        app_headers: Mapping[str, str] | None = None,
        timeout: float = 30.0,
        validate_responses: bool = True,
        max_retries: int = 2,
        backoff_base: float = 0.25,
        config: ClientConfig | None = None,
        registry: SchemaRegistry | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        if config is None:
            resolved_base_url = base_url or os.environ.get("INCIDENTIQ_BASE_URL")
            resolved_api_token = api_token or os.environ.get("INCIDENTIQ_API_TOKEN")
            if not resolved_base_url or not resolved_api_token:
                raise ConfigurationError(
                    "base_url and api_token are required (or set INCIDENTIQ_BASE_URL and "
                    "INCIDENTIQ_API_TOKEN)."
                )
            resolved_auth_mode = _normalize_auth_mode(auth_mode)
            config = ClientConfig(
                base_url=resolved_base_url.rstrip("/"),
                api_token=resolved_api_token,
                site_id=site_id,
                client_header=client_header,
                auth_mode=resolved_auth_mode,
                app_headers=_normalize_app_headers(app_headers),
                timeout=timeout,
                validate_responses=validate_responses,
                max_retries=max_retries,
                backoff_base=backoff_base,
            )

        self._config = config
        self._registry = registry or build_schema_registry(load_stoplight_documents())
        self._response_validator = ResponseSchemaValidator(self._registry)
        self._http = http_client or httpx.AsyncClient(timeout=config.timeout)
        self._logger = logging.getLogger("incident_py_q.client")

        self._sdk: SDKArtifacts = build_sdk(client=self, registry=self._registry, async_mode=True)
        for namespace_name, namespace_obj in self._sdk.namespaces.items():
            setattr(self, namespace_name, namespace_obj)
        self.apps = AsyncAppsNamespace(self)

    @classmethod
    def from_env(cls) -> AsyncClient:
        """Build an async client from standard runtime environment variables."""
        return cls(config=ClientConfig.from_env(env=dict(os.environ)))

    @classmethod
    def from_test_env(cls) -> AsyncClient:
        """Build an async client from integration test environment variables."""
        return cls(config=ClientConfig.from_env(env=dict(os.environ), test_mode=True))

    @property
    def config(self) -> ClientConfig:
        """Return immutable normalized runtime configuration."""
        return self._config

    def sdk_inventory(self) -> list[dict[str, str]]:
        """Return a stable inventory of generated SDK operations."""
        return list(self._sdk.inventory)

    def __getattr__(self, name: str) -> Any:
        namespace = self._sdk.namespaces.get(name)
        if namespace is not None:
            return namespace
        raise AttributeError(name)

    async def close(self) -> None:
        """Close the underlying async HTTP connection pool."""
        await self._http.aclose()

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | list[Any] | None:
        """Send an HTTP request and validate successful JSON payloads by contract."""
        rendered_path = render_path(path, dict(path_params) if path_params else None)
        operation = self._registry.match_operation(method, rendered_path)
        return await self._request_with_operation(
            method=method,
            rendered_path=rendered_path,
            operation=operation,
            params=dict(params) if params else None,
            json_body=json,
            headers=dict(headers) if headers else None,
            timeout=timeout,
        )

    async def _request_from_operation(
        self,
        operation: OperationSpec,
        *,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> dict[str, Any] | list[Any] | None:
        rendered_path = render_path(operation.path_template, path_params)
        return await self._request_with_operation(
            method=operation.method,
            rendered_path=rendered_path,
            operation=operation,
            params=params,
            json_body=json_body,
            headers=headers,
            timeout=timeout,
        )

    async def _request_with_operation(
        self,
        *,
        method: str,
        rendered_path: str,
        operation: OperationSpec | None,
        params: dict[str, Any] | None,
        json_body: Any | None,
        headers: dict[str, str] | None,
        timeout: float | None,
    ) -> dict[str, Any] | list[Any] | None:
        method_upper = method.upper()
        url = _build_url(self._config.base_url, rendered_path)
        merged_headers = _merge_headers(self._config, headers)
        request_timeout = timeout if timeout is not None else self._config.timeout
        can_retry = method_is_idempotent(method_upper)

        self._logger.debug(
            "incidentiq.request.start",
            extra={
                "method": method_upper,
                "path": rendered_path,
                "params": params or {},
                "headers": redact_headers(merged_headers),
            },
        )

        for attempt in range(self._config.max_retries + 1):
            try:
                response = await self._http.request(
                    method_upper,
                    url,
                    params=params,
                    json=json_body,
                    headers=merged_headers,
                    timeout=request_timeout,
                )

                if (
                    should_retry_status(response.status_code)
                    and can_retry
                    and attempt < self._config.max_retries
                ):
                    delay = compute_backoff_seconds(attempt, self._config.backoff_base)
                    await asyncio.sleep(delay)
                    continue

                response.raise_for_status()
                payload = _decode_payload(response)
                if (
                    payload is not None
                    and self._config.validate_responses
                    and operation is not None
                ):
                    self._response_validator.validate(
                        operation,
                        status_code=response.status_code,
                        payload=payload,
                    )

                self._logger.debug(
                    "incidentiq.request.success",
                    extra={
                        "method": method_upper,
                        "path": rendered_path,
                        "status_code": response.status_code,
                    },
                )
                return payload

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code
                if should_retry_status(status_code) and can_retry and attempt < self._config.max_retries:
                    delay = compute_backoff_seconds(attempt, self._config.backoff_base)
                    await asyncio.sleep(delay)
                    continue
                self._logger.warning(
                    "incidentiq.request.http_error",
                    extra={
                        "method": method_upper,
                        "path": rendered_path,
                        "status_code": status_code,
                    },
                )
                raise
            except httpx.RequestError:
                if can_retry and attempt < self._config.max_retries:
                    delay = compute_backoff_seconds(attempt, self._config.backoff_base)
                    await asyncio.sleep(delay)
                    continue
                self._logger.warning(
                    "incidentiq.request.transport_error",
                    extra={"method": method_upper, "path": rendered_path},
                )
                raise

        raise RuntimeError("Request loop exhausted unexpectedly")


def _build_url(base_url: str, rendered_path: str) -> str:
    if rendered_path.startswith("http://") or rendered_path.startswith("https://"):
        return rendered_path
    safe_path = rendered_path if rendered_path.startswith("/") else f"/{rendered_path}"
    return urljoin(f"{base_url}/", safe_path.lstrip("/"))


def _normalize_auth_mode(auth_mode: str) -> AuthMode:
    normalized = auth_mode.lower()
    if normalized not in {"bearer", "raw"}:
        raise ConfigurationError(
            f"Unsupported auth mode '{auth_mode}'. Expected 'bearer' or 'raw'."
        )
    return cast(AuthMode, normalized)


def _merge_headers(config: ClientConfig, headers: Mapping[str, str] | None) -> dict[str, str]:
    merged: dict[str, str] = {
        "Authorization": build_authorization_value(config.api_token, config.auth_mode),
        "Client": config.client_header,
    }
    if config.site_id:
        merged["SiteId"] = config.site_id
    if headers:
        merged.update(headers)
    return merged


def _normalize_app_headers(app_headers: Mapping[str, str] | None) -> dict[str, str] | None:
    if app_headers is None:
        return None
    normalized: dict[str, str] = {}
    for key, value in app_headers.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ConfigurationError("app_headers must be a mapping of string keys to string values.")
        normalized[key] = value
    return normalized or None


def _decode_payload(response: httpx.Response) -> dict[str, Any] | list[Any] | None:
    if response.status_code == 204:
        return None
    if not response.content:
        return None
    content_type = response.headers.get("content-type", "")
    if "json" in content_type.lower():
        data = response.json()
        if isinstance(data, (dict, list)):
            return data
        return None
    try:
        data = response.json()
    except ValueError:
        return None
    if isinstance(data, (dict, list)):
        return data
    return None
