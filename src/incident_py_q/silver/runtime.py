"""Runtime support for Silver-path undocumented SDK methods."""

from __future__ import annotations

import inspect
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Protocol
from urllib.parse import urlsplit

from incident_py_q.apps import (
    AppsNamespace,
    AsyncAppsNamespace,
    build_app_method_metadata,
)
from incident_py_q.config import ClientConfig

from .inventory import SilverMethodMetadata, SilverParameterMetadata, load_silver_inventory

JSONPayload = dict[str, Any] | list[Any] | None


class _SyncRequestClient(Protocol):
    @property
    def config(self) -> ClientConfig: ...

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
    ) -> JSONPayload: ...


class _AsyncRequestClient(Protocol):
    @property
    def config(self) -> ClientConfig: ...

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
    ) -> JSONPayload: ...


@dataclass(slots=True, frozen=True)
class SilverArtifacts:
    """Runtime Silver namespace tree and serialized inventories."""

    root: SilverRootNamespace
    inventory: list[dict[str, Any]]
    metadata: tuple[SilverMethodMetadata, ...]


def _tenant_origin(base_url: str) -> str:
    parsed = urlsplit(base_url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid tenant base URL {base_url!r}")
    return f"{parsed.scheme}://{parsed.netloc}"


def _absolute_silver_url(base_url: str, path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        return path
    if path.startswith("/apps/") or path.startswith("/api/v1.0/"):
        return f"{_tenant_origin(base_url)}{path}"
    return path


def _silver_headers(config: ClientConfig, method: SilverMethodMetadata) -> dict[str, str] | None:
    if not method.uses_app_headers or not config.app_headers:
        return None
    return dict(config.app_headers)


def _annotation_for_parameter(parameter: SilverParameterMetadata) -> Any:
    normalized = parameter.type_display.replace(" ", "")
    if normalized in {"bool", "bool|None"}:
        return bool
    if normalized in {"int", "int|None"}:
        return int
    if normalized in {"float", "float|None"}:
        return float
    if normalized in {"str", "str|None"}:
        return str
    return Any


def _build_signature(parameters: tuple[SilverParameterMetadata, ...]) -> inspect.Signature:
    signature_parameters: list[inspect.Parameter] = []
    for parameter in parameters:
        default = inspect._empty if parameter.required else None
        signature_parameters.append(
            inspect.Parameter(
                parameter.python_name,
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=default,
                annotation=_annotation_for_parameter(parameter),
            )
        )
    signature_parameters.append(
        inspect.Parameter(
            "timeout",
            kind=inspect.Parameter.KEYWORD_ONLY,
            default=None,
            annotation=float | None,
        )
    )
    return inspect.Signature(parameters=signature_parameters)


def format_silver_docstring(metadata: SilverMethodMetadata, *, async_mode: bool) -> str:
    """Build a verbose docstring explaining why this route is Silver-only."""
    call_prefix = "await " if async_mode else ""
    lines = [
        metadata.summary,
        "",
        metadata.description,
        "",
        f"HTTP route: {metadata.http_method} {metadata.route}",
        "Provenance: Silver (HAR-derived undocumented route)",
        "",
        "Why this method is separate from Golden paths:",
        (
            "Stoplight controller contracts are treated as the Golden source of truth for the SDK. "
            "This route remains on the Silver surface because no bundled Stoplight contract "
            "defines it, so the SDK exposes it explicitly instead of letting undocumented behavior "
            "silently override a Golden method."
        ),
        "",
        "Parameters:",
    ]
    if metadata.parameters:
        for parameter in metadata.parameters:
            requirement = "required" if parameter.required else "optional"
            lines.append(
                f"- `{parameter.python_name}` ({parameter.type_display}, {requirement}, "
                f"{parameter.location} -> `{parameter.api_name}`). {parameter.description}"
            )
    else:
        lines.append("- This route does not define inferred parameters.")
    lines.extend(
        [
            "",
            "Returns:",
            f"- `{call_prefix}client.silver.{metadata.namespace}.{metadata.method_name}(...)` returns "
            "`dict[str, Any] | list[Any] | None`.",
            f"- `{call_prefix}client.silver.{metadata.namespace}.{metadata.method_name}.raw(...)` returns "
            "`dict[str, Any] | list[Any] | None`.",
        ]
    )
    return "\n".join(lines)


class SilverNamespaceBase:
    """Namespace object that can hold both methods and child namespaces."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._methods: dict[str, Any] = {}
        self._namespaces: dict[str, Any] = {}

    def _register_method(self, name: str, method: Any) -> None:
        self._methods[name] = method
        setattr(self, name, method)

    def _register_namespace(self, name: str, namespace: Any) -> None:
        self._namespaces[name] = namespace
        setattr(self, name, namespace)

    def list_methods(self) -> list[str]:
        """Return available Silver method names for this namespace."""
        return sorted(self._methods)

    def list_namespaces(self) -> list[str]:
        """Return nested child namespace names."""
        return sorted(self._namespaces)

    def __dir__(self) -> list[str]:
        return sorted({*super().__dir__(), *self._methods, *self._namespaces})


class SilverRootNamespace(SilverNamespaceBase):
    """Root `client.silver` namespace."""


class SilverGenericNamespace(SilverNamespaceBase):
    """Generic nested Silver namespace."""


class SilverAppsNamespace(AppsNamespace, SilverNamespaceBase):
    """Silver apps namespace with legacy app services plus generated routes."""

    def __init__(self, client: _SyncRequestClient) -> None:
        AppsNamespace.__init__(self, client)
        SilverNamespaceBase.__init__(self, "apps")


class AsyncSilverAppsNamespace(AsyncAppsNamespace, SilverNamespaceBase):
    """Async Silver apps namespace with legacy app services plus generated routes."""

    def __init__(self, client: _AsyncRequestClient) -> None:
        AsyncAppsNamespace.__init__(self, client)
        SilverNamespaceBase.__init__(self, "apps")


class SilverOperationMethod:
    """Sync Silver-path callable."""

    def __init__(self, *, client: _SyncRequestClient, metadata: SilverMethodMetadata) -> None:
        self._client = client
        self.metadata = metadata
        self.__name__ = metadata.method_name
        self.__signature__ = _build_signature(metadata.parameters)
        self.__doc__ = format_silver_docstring(metadata, async_mode=False)

    def __call__(self, **kwargs: Any) -> JSONPayload:
        return self.raw(**kwargs)

    def raw(self, **kwargs: Any) -> JSONPayload:
        bound = self.__signature__.bind(**kwargs)
        timeout = bound.arguments.pop("timeout", None)
        path_params, query_params, json_body = _split_request_arguments(self.metadata, bound.arguments)
        return self._client.request(
            self.metadata.http_method,
            _absolute_silver_url(self._client.config.base_url, self.metadata.route),
            path_params=path_params or None,
            params=query_params or None,
            json=json_body,
            headers=_silver_headers(self._client.config, self.metadata),
            timeout=timeout,
        )


class AsyncSilverOperationMethod:
    """Async Silver-path callable."""

    def __init__(self, *, client: _AsyncRequestClient, metadata: SilverMethodMetadata) -> None:
        self._client = client
        self.metadata = metadata
        self.__name__ = metadata.method_name
        self.__signature__ = _build_signature(metadata.parameters)
        self.__doc__ = format_silver_docstring(metadata, async_mode=True)

    async def __call__(self, **kwargs: Any) -> JSONPayload:
        return await self.raw(**kwargs)

    async def raw(self, **kwargs: Any) -> JSONPayload:
        bound = self.__signature__.bind(**kwargs)
        timeout = bound.arguments.pop("timeout", None)
        path_params, query_params, json_body = _split_request_arguments(self.metadata, bound.arguments)
        return await self._client.request(
            self.metadata.http_method,
            _absolute_silver_url(self._client.config.base_url, self.metadata.route),
            path_params=path_params or None,
            params=query_params or None,
            json=json_body,
            headers=_silver_headers(self._client.config, self.metadata),
            timeout=timeout,
        )


def build_silver_metadata() -> tuple[SilverMethodMetadata, ...]:
    """Load checked-in Silver metadata used by runtime, docs, and stubs."""
    return load_silver_inventory()


def build_silver_sdk(*, client: Any, async_mode: bool) -> SilverArtifacts:
    """Build the explicit `client.silver` namespace tree."""
    metadata = build_silver_metadata()
    root = SilverRootNamespace("silver")
    apps_namespace: SilverAppsNamespace | AsyncSilverAppsNamespace
    apps_namespace = AsyncSilverAppsNamespace(client) if async_mode else SilverAppsNamespace(client)
    root._register_namespace("apps", apps_namespace)

    namespace_lookup: dict[tuple[str, ...], Any] = {("apps",): apps_namespace}
    inventory: list[dict[str, Any]] = []

    # These legacy app helper services are intentionally exposed both as `client.apps` and as
    # `client.silver.apps`. The alias keeps existing integrations working while making it explicit
    # in the new SDK surface that app-path behavior is Silver and supplemental.
    for service_name in ("registry", "microsoft_intune", "mosyle", "google_device_data"):
        apps_namespace._register_namespace(service_name, getattr(apps_namespace, service_name))

    for method in metadata:
        namespace = _ensure_namespace(
            root=root,
            namespace_lookup=namespace_lookup,
            namespace_path=method.namespace_path,
            async_mode=async_mode,
            client=client,
        )
        method_obj: Any = (
            AsyncSilverOperationMethod(client=client, metadata=method)
            if async_mode
            else SilverOperationMethod(client=client, metadata=method)
        )
        if hasattr(namespace, "_register_method"):
            namespace._register_method(method.method_name, method_obj)
        else:
            setattr(namespace, method.method_name, method_obj)
        inventory.append(
            {
                "provenance": "silver",
                "namespace": method.namespace,
                "name": method.method_name,
                "http_method": method.http_method,
                "path": method.route,
            }
        )

    for app_method in build_app_method_metadata():
        inventory.append(
            {
                "provenance": "silver",
                "namespace": f"apps.{app_method.service_name}",
                "name": app_method.method_name,
                "http_method": app_method.http_method,
                "path": app_method.route,
            }
        )

    return SilverArtifacts(
        root=root,
        inventory=sorted(inventory, key=str),
        metadata=metadata,
    )


def _ensure_namespace(
    *,
    root: SilverRootNamespace,
    namespace_lookup: dict[tuple[str, ...], Any],
    namespace_path: tuple[str, ...],
    async_mode: bool,
    client: Any,
) -> Any:
    current_path: list[str] = []
    parent: Any = root
    for segment in namespace_path:
        current_path.append(segment)
        key = tuple(current_path)
        existing = namespace_lookup.get(key)
        if existing is not None:
            parent = existing
            continue

        if current_path[:1] == ["apps"] and len(current_path) == 2 and hasattr(parent, segment):
            existing_namespace = getattr(parent, segment)
            parent._register_namespace(segment, existing_namespace)
            namespace_lookup[key] = existing_namespace
            parent = existing_namespace
            continue

        if key == ("apps",):
            namespace_obj: Any = (
                AsyncSilverAppsNamespace(client) if async_mode else SilverAppsNamespace(client)
            )
        else:
            namespace_obj = SilverGenericNamespace(segment)
        parent._register_namespace(segment, namespace_obj)
        namespace_lookup[key] = namespace_obj
        parent = namespace_obj
    return parent


def _split_request_arguments(
    metadata: SilverMethodMetadata,
    arguments: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], Any | None]:
    path_params: dict[str, Any] = {}
    query_params: dict[str, Any] = {}
    json_body: Any | None = None

    for parameter in metadata.parameters:
        value = arguments.get(parameter.python_name)
        if value is None:
            continue
        if parameter.location == "path":
            path_params[parameter.python_name] = value
        elif parameter.location == "query":
            query_params[parameter.api_name] = value
        elif parameter.location == "body":
            if parameter.python_name == "json_body":
                json_body = value
            else:
                if not isinstance(json_body, dict):
                    json_body = {}
                json_body[parameter.api_name] = value

    return path_params, query_params, json_body
