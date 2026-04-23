"""Runtime support for Silver-path undocumented SDK methods."""

from __future__ import annotations

import asyncio
import inspect
import mimetypes
import time
from collections.abc import Mapping
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlsplit

from incident_py_q.apps import (
    AppsNamespace,
    AsyncAppsNamespace,
    build_app_method_metadata,
)
from incident_py_q.config import ClientConfig
from incident_py_q.media import prepare_png_upload

from .inventory import SilverMethodMetadata, SilverParameterMetadata, load_silver_inventory

JSONPayload = dict[str, Any] | list[Any] | None
PreparedFiles = dict[str, tuple[str, Any, str]]
_PROFILE_PICTURE_UPLOAD = ("POST", "/api/v1.0/profiles/{user_id}/picture")
_DIRECT_USER_ROUTE = "/api/v1.0/users/{user_id}"
_DEFAULT_CONSISTENCY_TIMEOUT = 10.0
_DEFAULT_CONSISTENCY_POLL_INTERVAL = 1.0
_ZERO_UUID = "00000000-0000-0000-0000-000000000000"
_REMOVE_PROFILE_PICTURE_REQUIRED_FIELDS = (
    "UserId",
    "IsDeleted",
    "SiteId",
    "ProductId",
    "CreatedDate",
    "ModifiedDate",
    "LocationId",
    "IsActive",
    "IsOnline",
    "IsOnlineLastUpdated",
    "RoleId",
    "AccountSetupProgress",
    "TrainingPercentComplete",
    "IsEmailVerified",
    "IsWelcomeEmailSent",
    "PreventProviderUpdates",
    "IsOutOfOffice",
    "Portal",
    "UpdateCustomFields",
)


class _SyncRequestClient(Protocol):
    @property
    def config(self) -> ClientConfig: ...

    @property
    def users(self) -> Any: ...

    def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        files: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> JSONPayload: ...

    def request_silver(
        self,
        metadata: SilverMethodMetadata,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        files: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> JSONPayload: ...


class _AsyncRequestClient(Protocol):
    @property
    def config(self) -> ClientConfig: ...

    @property
    def users(self) -> Any: ...

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        files: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> JSONPayload: ...

    async def request_silver(
        self,
        metadata: SilverMethodMetadata,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any | None = None,
        files: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> JSONPayload: ...


@dataclass(slots=True, frozen=True)
class SilverArtifacts:
    """Runtime Silver namespace tree and serialized inventories."""

    root: SilverRootNamespace
    inventory: list[dict[str, Any]]
    metadata: tuple[SilverMethodMetadata, ...]


@dataclass(slots=True, frozen=True)
class SilverManualParameterMetadata:
    """Documentation metadata for one non-HAR Silver helper parameter."""

    python_name: str
    api_name: str
    location: str
    required: bool
    type_display: str
    description: str


@dataclass(slots=True, frozen=True)
class SilverManualMethodMetadata:
    """Documentation metadata for one manual Silver helper."""

    namespace_path: tuple[str, ...]
    method_name: str
    summary: str
    description: str
    parameters: tuple[SilverManualParameterMetadata, ...]
    typed_return: str
    raw_return: str
    response_model: str | None = None
    backing_routes: tuple[str, ...] = ()

    @property
    def namespace(self) -> str:
        """Return the dot-qualified namespace path without the Silver root."""
        return ".".join(self.namespace_path)


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
    if "PathLike[" in parameter.type_display or "PathLike" in normalized:
        return str | PathLike[str]
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
    if _is_profile_picture_upload(metadata):
        lines.extend(
            [
                "",
                "Behavior notes:",
                (
                    "This route is profile-specific because the SDK prepares the final avatar bitmap "
                    "inside `post_profile_picture(...)`: non-square inputs are center-cropped, then "
                    "converted to PNG and reduced under the 1 MB limit before upload."
                ),
                (
                    "Set `wait_for_consistency=True` when your workflow needs the SDK to poll user "
                    "readback until the new `PhotoId` becomes visible. The default stays fast "
                    "because some tenants reflect the write slightly after the upload call returns."
                ),
            ]
        )
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


def format_manual_silver_docstring(
    metadata: SilverManualMethodMetadata,
    *,
    async_mode: bool,
) -> str:
    """Build a verbose docstring for a manual Silver helper."""
    call_prefix = "await " if async_mode else ""
    lines = [
        metadata.summary,
        "",
        metadata.description,
        "",
        "Provenance: Silver manual helper",
    ]
    if metadata.backing_routes:
        lines.extend(
            [
                "Backing routes:",
                *(f"- `{route}`" for route in metadata.backing_routes),
            ]
        )
    lines.extend(["", "Parameters:"])
    for parameter in metadata.parameters:
        requirement = "required" if parameter.required else "optional"
        lines.append(
            f"- `{parameter.python_name}` ({parameter.type_display}, {requirement}, "
            f"{parameter.location} -> `{parameter.api_name}`). {parameter.description}"
        )
    if metadata.namespace_path == ("profiles",) and metadata.method_name == "remove_profile_picture":
        lines.extend(
            [
                "",
                "Behavior notes:",
                (
                    "This helper is implemented as a safe user-update workflow because Incident IQ "
                    "does not publish a dedicated remove-profile-picture route."
                ),
                (
                    "The helper tries the typed Golden user getter first, then falls back to the "
                    "explicit `/api/v1.0/users/{user_id}` JSON route on tenants where the Golden "
                    "path does not yield usable user JSON."
                ),
                (
                    "Set `wait_for_consistency=True` when your workflow needs the SDK to wait for "
                    "`PhotoId` readback to clear before continuing."
                ),
            ]
        )
    lines.extend(
        [
            "",
            "Returns:",
            f"- `{call_prefix}client.silver.{metadata.namespace}.{metadata.method_name}(...)` returns "
            f"`{metadata.typed_return}`.",
            (
                "- The helper does not expose a public `.raw(...)` method; `.raw(...)` is kept as an "
                "internal fallback only if the typed Golden route path cannot carry the required "
                "payload shape."
            ),
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
        path_params, query_params, json_body, file_params = _split_request_arguments(
            self.metadata, bound.arguments
        )
        files, opened_handles = _prepare_silver_file_uploads(self.metadata, file_params)
        try:
            return self._client.request_silver(
                self.metadata,
                path_params=path_params or None,
                params=query_params or None,
                json=json_body,
                files=files or None,
                headers=_silver_headers(self._client.config, self.metadata),
                timeout=timeout,
            )
        finally:
            for handle in opened_handles:
                handle.close()


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
        path_params, query_params, json_body, file_params = _split_request_arguments(
            self.metadata, bound.arguments
        )
        files, opened_handles = _prepare_silver_file_uploads(self.metadata, file_params)
        try:
            return await self._client.request_silver(
                self.metadata,
                path_params=path_params or None,
                params=query_params or None,
                json=json_body,
                files=files or None,
                headers=_silver_headers(self._client.config, self.metadata),
                timeout=timeout,
            )
        finally:
            for handle in opened_handles:
                handle.close()


class SilverProfilePictureUploadMethod:
    """Sync Silver helper for uploading and optionally validating a profile picture."""

    def __init__(self, *, client: _SyncRequestClient, metadata: SilverMethodMetadata) -> None:
        self._client = client
        self.metadata = metadata
        self.__name__ = metadata.method_name
        self.__signature__ = inspect.Signature(
            parameters=[
                inspect.Parameter("user_id", kind=inspect.Parameter.KEYWORD_ONLY, annotation=str),
                inspect.Parameter(
                    "file",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    annotation=str | PathLike[str],
                ),
                inspect.Parameter(
                    "wait_for_consistency",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=False,
                    annotation=bool,
                ),
                inspect.Parameter(
                    "consistency_timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_TIMEOUT,
                    annotation=float,
                ),
                inspect.Parameter(
                    "consistency_poll_interval",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_POLL_INTERVAL,
                    annotation=float,
                ),
                inspect.Parameter(
                    "timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation=float | None,
                ),
            ]
        )
        self.__doc__ = format_silver_docstring(metadata, async_mode=False)

    def __call__(
        self,
        *,
        user_id: str,
        file: str | PathLike[str],
        wait_for_consistency: bool = False,
        consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
        consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
        timeout: float | None = None,
    ) -> JSONPayload:
        return self.raw(
            user_id=user_id,
            file=file,
            wait_for_consistency=wait_for_consistency,
            consistency_timeout=consistency_timeout,
            consistency_poll_interval=consistency_poll_interval,
            timeout=timeout,
        )

    def raw(
        self,
        *,
        user_id: str,
        file: str | PathLike[str],
        wait_for_consistency: bool = False,
        consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
        consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
        timeout: float | None = None,
    ) -> JSONPayload:
        starting_photo_id = None
        if wait_for_consistency:
            starting_photo_id = _extract_photo_id(
                _get_profile_user_response_sync(self._client, user_id=user_id, timeout=timeout)
            )
        response = _request_profile_picture_upload_sync(
            self._client,
            self.metadata,
            user_id=user_id,
            file=file,
            timeout=timeout,
        )
        if wait_for_consistency:
            expected_photo_id = _extract_upload_file_id(response)
            _wait_for_profile_photo_state_sync(
                self._client,
                user_id=user_id,
                timeout=timeout,
                consistency_timeout=consistency_timeout,
                consistency_poll_interval=consistency_poll_interval,
                predicate=_build_upload_consistency_predicate(
                    expected_photo_id=expected_photo_id,
                    starting_photo_id=starting_photo_id,
                ),
                expectation=(
                    f"PhotoId to match uploaded FileId {expected_photo_id!r}"
                    if expected_photo_id is not None
                    else "PhotoId to change to a non-null value after upload"
                ),
            )
        return response


class AsyncSilverProfilePictureUploadMethod:
    """Async Silver helper for uploading and optionally validating a profile picture."""

    def __init__(self, *, client: _AsyncRequestClient, metadata: SilverMethodMetadata) -> None:
        self._client = client
        self.metadata = metadata
        self.__name__ = metadata.method_name
        self.__signature__ = inspect.Signature(
            parameters=[
                inspect.Parameter("user_id", kind=inspect.Parameter.KEYWORD_ONLY, annotation=str),
                inspect.Parameter(
                    "file",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    annotation=str | PathLike[str],
                ),
                inspect.Parameter(
                    "wait_for_consistency",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=False,
                    annotation=bool,
                ),
                inspect.Parameter(
                    "consistency_timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_TIMEOUT,
                    annotation=float,
                ),
                inspect.Parameter(
                    "consistency_poll_interval",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_POLL_INTERVAL,
                    annotation=float,
                ),
                inspect.Parameter(
                    "timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation=float | None,
                ),
            ]
        )
        self.__doc__ = format_silver_docstring(metadata, async_mode=True)

    async def __call__(
        self,
        *,
        user_id: str,
        file: str | PathLike[str],
        wait_for_consistency: bool = False,
        consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
        consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
        timeout: float | None = None,
    ) -> JSONPayload:
        return await self.raw(
            user_id=user_id,
            file=file,
            wait_for_consistency=wait_for_consistency,
            consistency_timeout=consistency_timeout,
            consistency_poll_interval=consistency_poll_interval,
            timeout=timeout,
        )

    async def raw(
        self,
        *,
        user_id: str,
        file: str | PathLike[str],
        wait_for_consistency: bool = False,
        consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
        consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
        timeout: float | None = None,
    ) -> JSONPayload:
        starting_photo_id = None
        if wait_for_consistency:
            starting_photo_id = _extract_photo_id(
                await _get_profile_user_response_async(self._client, user_id=user_id, timeout=timeout)
            )
        response = await _request_profile_picture_upload_async(
            self._client,
            self.metadata,
            user_id=user_id,
            file=file,
            timeout=timeout,
        )
        if wait_for_consistency:
            expected_photo_id = _extract_upload_file_id(response)
            await _wait_for_profile_photo_state_async(
                self._client,
                user_id=user_id,
                timeout=timeout,
                consistency_timeout=consistency_timeout,
                consistency_poll_interval=consistency_poll_interval,
                predicate=_build_upload_consistency_predicate(
                    expected_photo_id=expected_photo_id,
                    starting_photo_id=starting_photo_id,
                ),
                expectation=(
                    f"PhotoId to match uploaded FileId {expected_photo_id!r}"
                    if expected_photo_id is not None
                    else "PhotoId to change to a non-null value after upload"
                ),
            )
        return response


class SilverRemoveProfilePictureMethod:
    """Sync Silver helper for clearing a user's profile picture safely."""

    def __init__(self, *, client: _SyncRequestClient, metadata: SilverManualMethodMetadata) -> None:
        self._client = client
        self.metadata = metadata
        self.__name__ = metadata.method_name
        self.__signature__ = inspect.Signature(
            parameters=[
                inspect.Parameter(
                    "user_id",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    annotation=str,
                ),
                inspect.Parameter(
                    "wait_for_consistency",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=False,
                    annotation=bool,
                ),
                inspect.Parameter(
                    "consistency_timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_TIMEOUT,
                    annotation=float,
                ),
                inspect.Parameter(
                    "consistency_poll_interval",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_POLL_INTERVAL,
                    annotation=float,
                ),
                inspect.Parameter(
                    "timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation=float | None,
                ),
            ]
        )
        self.__doc__ = format_manual_silver_docstring(metadata, async_mode=False)

    def __call__(
        self,
        *,
        user_id: str,
        timeout: float | None = None,
        wait_for_consistency: bool = False,
        consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
        consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
    ) -> Any:
        return _remove_profile_picture_sync(
            self._client,
            user_id=user_id,
            timeout=timeout,
            wait_for_consistency=wait_for_consistency,
            consistency_timeout=consistency_timeout,
            consistency_poll_interval=consistency_poll_interval,
        )


class AsyncSilverRemoveProfilePictureMethod:
    """Async Silver helper for clearing a user's profile picture safely."""

    def __init__(self, *, client: _AsyncRequestClient, metadata: SilverManualMethodMetadata) -> None:
        self._client = client
        self.metadata = metadata
        self.__name__ = metadata.method_name
        self.__signature__ = inspect.Signature(
            parameters=[
                inspect.Parameter(
                    "user_id",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    annotation=str,
                ),
                inspect.Parameter(
                    "wait_for_consistency",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=False,
                    annotation=bool,
                ),
                inspect.Parameter(
                    "consistency_timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_TIMEOUT,
                    annotation=float,
                ),
                inspect.Parameter(
                    "consistency_poll_interval",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=_DEFAULT_CONSISTENCY_POLL_INTERVAL,
                    annotation=float,
                ),
                inspect.Parameter(
                    "timeout",
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation=float | None,
                ),
            ]
        )
        self.__doc__ = format_manual_silver_docstring(metadata, async_mode=True)

    async def __call__(
        self,
        *,
        user_id: str,
        timeout: float | None = None,
        wait_for_consistency: bool = False,
        consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
        consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
    ) -> Any:
        return await _remove_profile_picture_async(
            self._client,
            user_id=user_id,
            timeout=timeout,
            wait_for_consistency=wait_for_consistency,
            consistency_timeout=consistency_timeout,
            consistency_poll_interval=consistency_poll_interval,
        )


def build_silver_metadata() -> tuple[SilverMethodMetadata, ...]:
    """Load checked-in Silver metadata used by runtime, docs, and stubs."""
    return load_silver_inventory()


def build_manual_silver_method_metadata() -> tuple[SilverManualMethodMetadata, ...]:
    """Return manual Silver helpers that intentionally wrap safer Golden workflows."""
    return (
        SilverManualMethodMetadata(
            namespace_path=("profiles",),
            method_name="remove_profile_picture",
            summary="Remove a user's profile picture by clearing `PhotoId` through the documented Golden user update route.",
            description=(
                "This helper exists on the Silver surface because Incident IQ exposes profile-picture "
                "removal as a user update workflow rather than as its own published profile route. "
                "The helper first tries the typed Golden `users.get_user(...)` method, then falls back "
                "to the explicit `/api/v1.0/users/{user_id}` JSON route if the tenant does not return "
                "usable user JSON through the Golden path. It builds the smallest proven-safe "
                "`UpdateUserRequest`: the required update fields copied exactly from the fetched user "
                "plus `PhotoId = None`. It intentionally does not repost the full user object, so "
                "unrelated user fields are not cleared by omission. Validation is opt-in because some "
                "tenants reflect `PhotoId` changes a moment after the write call returns. `.raw(...)` "
                "stays an internal fallback of last resort, not the normal compatibility path."
            ),
            parameters=(
                SilverManualParameterMetadata(
                    python_name="user_id",
                    api_name="user_id",
                    location="path",
                    required=True,
                    type_display="str",
                    description="User identifier whose profile picture should be removed.",
                ),
                SilverManualParameterMetadata(
                    python_name="wait_for_consistency",
                    api_name="wait_for_consistency",
                    location="client",
                    required=False,
                    type_display="bool",
                    description=(
                        "When `True`, poll user readback until `PhotoId` becomes `None` or raise "
                        "`TimeoutError` if the tenant does not converge in time."
                    ),
                ),
                SilverManualParameterMetadata(
                    python_name="consistency_timeout",
                    api_name="consistency_timeout",
                    location="client",
                    required=False,
                    type_display="float",
                    description=(
                        "Maximum number of seconds to wait for readback convergence when "
                        "`wait_for_consistency=True`."
                    ),
                ),
                SilverManualParameterMetadata(
                    python_name="consistency_poll_interval",
                    api_name="consistency_poll_interval",
                    location="client",
                    required=False,
                    type_display="float",
                    description=(
                        "Polling interval in seconds between user readback checks when "
                        "`wait_for_consistency=True`."
                    ),
                ),
            ),
            typed_return="ItemUpdateResponseOfUser",
            raw_return="dict[str, Any] | list[Any] | None",
            response_model="ItemUpdateResponseOfUser",
            backing_routes=(
                "GET /api/v1.0/users/{user_id}",
                "POST /api/v1.0/users/{user_id}",
            ),
        ),
    )


def build_silver_sdk(*, client: Any, async_mode: bool) -> SilverArtifacts:
    """Build the explicit `client.silver` namespace tree."""
    metadata = build_silver_metadata()
    manual_metadata = build_manual_silver_method_metadata()
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
        method_obj: Any
        if _is_profile_picture_upload(method):
            method_obj = (
                AsyncSilverProfilePictureUploadMethod(client=client, metadata=method)
                if async_mode
                else SilverProfilePictureUploadMethod(client=client, metadata=method)
            )
        else:
            method_obj = (
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

    for manual_method in manual_metadata:
        namespace = _ensure_namespace(
            root=root,
            namespace_lookup=namespace_lookup,
            namespace_path=manual_method.namespace_path,
            async_mode=async_mode,
            client=client,
        )
        method_obj = _build_manual_silver_method(
            client=client,
            metadata=manual_method,
            async_mode=async_mode,
        )
        if hasattr(namespace, "_register_method"):
            namespace._register_method(manual_method.method_name, method_obj)
        else:
            setattr(namespace, manual_method.method_name, method_obj)
        inventory.append(
            {
                "provenance": "silver",
                "namespace": manual_method.namespace,
                "name": manual_method.method_name,
                "kind": "manual_helper",
                "backing_routes": list(manual_method.backing_routes),
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


def _build_manual_silver_method(
    *,
    client: Any,
    metadata: SilverManualMethodMetadata,
    async_mode: bool,
) -> Any:
    if metadata.namespace_path == ("profiles",) and metadata.method_name == "remove_profile_picture":
        return (
            AsyncSilverRemoveProfilePictureMethod(client=client, metadata=metadata)
            if async_mode
            else SilverRemoveProfilePictureMethod(client=client, metadata=metadata)
        )
    raise ValueError(f"Unsupported Silver manual helper {metadata.namespace}.{metadata.method_name!r}.")


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
) -> tuple[dict[str, Any], dict[str, Any], Any | None, dict[str, Any]]:
    path_params: dict[str, Any] = {}
    query_params: dict[str, Any] = {}
    json_body: Any | None = None
    files: dict[str, Any] = {}

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
        elif parameter.location == "file":
            files[parameter.api_name] = value

    return path_params, query_params, json_body, files


def _coerce_file_uploads(file_params: Mapping[str, Any]) -> tuple[PreparedFiles, list[Any]]:
    prepared: PreparedFiles = {}
    opened_handles: list[Any] = []
    for field_name, value in file_params.items():
        if isinstance(value, (str, PathLike)):
            path = Path(value)
        else:
            raise TypeError(
                f"Silver file parameter '{field_name}' must be a str or PathLike path, "
                f"got {type(value).__name__}."
            )
        handle = path.open("rb")
        opened_handles.append(handle)
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        prepared[field_name] = (path.name, handle, content_type)
    return prepared, opened_handles


def _prepare_silver_file_uploads(
    metadata: SilverMethodMetadata,
    file_params: Mapping[str, Any],
) -> tuple[PreparedFiles, list[Any]]:
    # The generic multipart helper intentionally stays dumb: it forwards local file paths as-is.
    # `post_profile_picture(...)` is the one explicit exception because the business rule is that
    # callers can hand the profile method a common local image format and the SDK itself will
    # prepare the final avatar bitmap before anything is sent over the wire. The resize HAR only
    # showed the profile-picture upload plus a later `GET /img/...?...w=150&h=150`, not a separate
    # persisted crop endpoint, so the SDK applies the centered square crop locally and then
    # normalizes the result to a size-limited PNG.
    if _is_profile_picture_upload(metadata):
        return _coerce_profile_picture_uploads(file_params), []
    return _coerce_file_uploads(file_params)


def _is_profile_picture_upload(metadata: SilverMethodMetadata) -> bool:
    return (metadata.http_method.upper(), metadata.route) == _PROFILE_PICTURE_UPLOAD


def _coerce_profile_picture_uploads(file_params: Mapping[str, Any]) -> PreparedFiles:
    prepared: PreparedFiles = {}
    for field_name, value in file_params.items():
        if not isinstance(value, (str, PathLike)):
            raise TypeError(
                f"Silver file parameter '{field_name}' must be a str or PathLike path, "
                f"got {type(value).__name__}."
            )
        prepared[field_name] = prepare_png_upload(value, crop_to_square=True)
    return prepared


def _model_dump(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(by_alias=True)
    return value


def _extract_user_item(response: Any) -> dict[str, Any]:
    payload = _model_dump(response)
    if not isinstance(payload, Mapping):
        raise ValueError("Expected user lookup response object.")
    item = _model_dump(payload.get("Item"))
    if not isinstance(item, Mapping):
        raise ValueError("Expected user lookup response to include an Item object.")
    return dict(item)


def _extract_photo_id(response: Any) -> Any:
    return _extract_user_item(response).get("PhotoId")


def _extract_upload_file_id(response: Any) -> Any:
    payload = _model_dump(response)
    if isinstance(payload, Mapping):
        item = payload.get("Item")
        if isinstance(item, Mapping):
            return item.get("FileId")
    return None


def _require_update_response(response: Any) -> Any:
    if response is None or (
        not isinstance(response, Mapping) and not hasattr(response, "model_dump")
    ):
        raise ValueError("Expected update response object.")
    return response


def _get_profile_user_response_sync(
    client: _SyncRequestClient,
    *,
    user_id: str,
    timeout: float | None,
) -> Any:
    try:
        response = client.users.get_user(user_id=user_id, timeout=timeout)
        _extract_user_item(response)
        return response
    except (AttributeError, TypeError, ValueError):
        pass

    try:
        response = client.request(
            "GET",
            _DIRECT_USER_ROUTE,
            path_params={"user_id": user_id},
            timeout=timeout,
        )
        _extract_user_item(response)
        return response
    except (TypeError, ValueError):
        pass

    raw_response = client.users.get_user.raw(user_id=user_id, timeout=timeout)
    _extract_user_item(raw_response)
    return raw_response


async def _get_profile_user_response_async(
    client: _AsyncRequestClient,
    *,
    user_id: str,
    timeout: float | None,
) -> Any:
    try:
        response = await client.users.get_user(user_id=user_id, timeout=timeout)
        _extract_user_item(response)
        return response
    except (AttributeError, TypeError, ValueError):
        pass

    try:
        response = await client.request(
            "GET",
            _DIRECT_USER_ROUTE,
            path_params={"user_id": user_id},
            timeout=timeout,
        )
        _extract_user_item(response)
        return response
    except (TypeError, ValueError):
        pass

    raw_response = await client.users.get_user.raw(user_id=user_id, timeout=timeout)
    _extract_user_item(raw_response)
    return raw_response


def _build_remove_profile_picture_payload(
    *,
    user_id: str,
    user_item: Mapping[str, Any],
) -> dict[str, Any]:
    missing = [
        field
        for field in _REMOVE_PROFILE_PICTURE_REQUIRED_FIELDS
        if field not in user_item
        and field not in {"ProductId", "TrainingPercentComplete", "UpdateCustomFields"}
    ]
    if missing:
        joined = ", ".join(sorted(missing))
        raise ValueError(
            "User lookup response did not include the required fields needed to remove the "
            f"profile picture safely: {joined}."
        )

    fetched_user_id = user_item.get("UserId")
    if fetched_user_id != user_id:
        raise ValueError(
            "User lookup returned a different UserId than the requested profile-picture removal "
            f"target: expected {user_id!r}, got {fetched_user_id!r}."
        )

    payload = {field: user_item[field] for field in _REMOVE_PROFILE_PICTURE_REQUIRED_FIELDS if field in user_item}
    site_payload = _model_dump(user_item.get("Site")) if user_item.get("Site") is not None else {}
    if not isinstance(site_payload, Mapping):
        site_payload = {}
    payload["ProductId"] = user_item.get("ProductId") or site_payload.get("ProductId") or _ZERO_UUID
    payload["TrainingPercentComplete"] = user_item.get("TrainingPercentComplete", 0)
    payload["UpdateCustomFields"] = user_item.get("UpdateCustomFields", False)
    payload["PhotoId"] = None
    return payload


def _build_upload_consistency_predicate(
    *,
    expected_photo_id: Any,
    starting_photo_id: Any,
) -> Any:
    if expected_photo_id is not None:
        return lambda photo_id: photo_id == expected_photo_id
    return lambda photo_id: photo_id is not None and photo_id != starting_photo_id


def _wait_for_profile_photo_state_sync(
    client: _SyncRequestClient,
    *,
    user_id: str,
    timeout: float | None,
    consistency_timeout: float,
    consistency_poll_interval: float,
    predicate: Any,
    expectation: str,
) -> Any:
    deadline = time.monotonic() + consistency_timeout
    last_photo_id = None
    while True:
        response = _get_profile_user_response_sync(client, user_id=user_id, timeout=timeout)
        last_photo_id = _extract_photo_id(response)
        if predicate(last_photo_id):
            return last_photo_id
        if time.monotonic() >= deadline:
            raise TimeoutError(
                "Profile-picture write call returned, but tenant readback did not converge within "
                f"{consistency_timeout:.1f}s. Expected {expectation}, last observed PhotoId "
                f"was {last_photo_id!r}."
            )
        time.sleep(consistency_poll_interval)


async def _wait_for_profile_photo_state_async(
    client: _AsyncRequestClient,
    *,
    user_id: str,
    timeout: float | None,
    consistency_timeout: float,
    consistency_poll_interval: float,
    predicate: Any,
    expectation: str,
) -> Any:
    deadline = time.monotonic() + consistency_timeout
    last_photo_id = None
    while True:
        response = await _get_profile_user_response_async(client, user_id=user_id, timeout=timeout)
        last_photo_id = _extract_photo_id(response)
        if predicate(last_photo_id):
            return last_photo_id
        if time.monotonic() >= deadline:
            raise TimeoutError(
                "Profile-picture write call returned, but tenant readback did not converge within "
                f"{consistency_timeout:.1f}s. Expected {expectation}, last observed PhotoId "
                f"was {last_photo_id!r}."
            )
        await asyncio.sleep(consistency_poll_interval)


def _request_profile_picture_upload_sync(
    client: _SyncRequestClient,
    metadata: SilverMethodMetadata,
    *,
    user_id: str,
    file: str | PathLike[str],
    timeout: float | None,
) -> JSONPayload:
    files, opened_handles = _prepare_silver_file_uploads(metadata, {"File": file})
    try:
        return client.request_silver(
            metadata,
            path_params={"user_id": user_id},
            files=files or None,
            headers=_silver_headers(client.config, metadata),
            timeout=timeout,
        )
    finally:
        for handle in opened_handles:
            handle.close()


async def _request_profile_picture_upload_async(
    client: _AsyncRequestClient,
    metadata: SilverMethodMetadata,
    *,
    user_id: str,
    file: str | PathLike[str],
    timeout: float | None,
) -> JSONPayload:
    files, opened_handles = _prepare_silver_file_uploads(metadata, {"File": file})
    try:
        return await client.request_silver(
            metadata,
            path_params={"user_id": user_id},
            files=files or None,
            headers=_silver_headers(client.config, metadata),
            timeout=timeout,
        )
    finally:
        for handle in opened_handles:
            handle.close()


def _remove_profile_picture_sync(
    client: _SyncRequestClient,
    *,
    user_id: str,
    timeout: float | None,
    wait_for_consistency: bool = False,
    consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
    consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
) -> Any:
    try:
        response = _get_profile_user_response_sync(client, user_id=user_id, timeout=timeout)
        user_item = _extract_user_item(response)
        payload = _build_remove_profile_picture_payload(user_id=user_id, user_item=user_item)
        try:
            result = _require_update_response(
                client.users.update_user(user_id=user_id, user=payload, timeout=timeout)
            )
        except (AttributeError, TypeError, ValueError):
            try:
                result = client.request(
                    "POST",
                    _DIRECT_USER_ROUTE,
                    path_params={"user_id": user_id},
                    json=payload,
                    timeout=timeout,
                )
                result = _require_update_response(result)
            except (TypeError, ValueError):
                result = client.users.update_user.raw(user_id=user_id, user=payload, timeout=timeout)
        if wait_for_consistency:
            _wait_for_profile_photo_state_sync(
                client,
                user_id=user_id,
                timeout=timeout,
                consistency_timeout=consistency_timeout,
                consistency_poll_interval=consistency_poll_interval,
                predicate=lambda photo_id: photo_id is None,
                expectation="PhotoId to become None after profile-picture removal",
            )
        return result
    except (AttributeError, TypeError, ValueError):
        raw_response = client.users.get_user.raw(user_id=user_id, timeout=timeout)
        user_item = _extract_user_item(raw_response)
        payload = _build_remove_profile_picture_payload(user_id=user_id, user_item=user_item)
        result = client.users.update_user.raw(user_id=user_id, user=payload, timeout=timeout)
        if wait_for_consistency:
            _wait_for_profile_photo_state_sync(
                client,
                user_id=user_id,
                timeout=timeout,
                consistency_timeout=consistency_timeout,
                consistency_poll_interval=consistency_poll_interval,
                predicate=lambda photo_id: photo_id is None,
                expectation="PhotoId to become None after profile-picture removal",
            )
        return result


async def _remove_profile_picture_async(
    client: _AsyncRequestClient,
    *,
    user_id: str,
    timeout: float | None,
    wait_for_consistency: bool = False,
    consistency_timeout: float = _DEFAULT_CONSISTENCY_TIMEOUT,
    consistency_poll_interval: float = _DEFAULT_CONSISTENCY_POLL_INTERVAL,
) -> Any:
    try:
        response = await _get_profile_user_response_async(client, user_id=user_id, timeout=timeout)
        user_item = _extract_user_item(response)
        payload = _build_remove_profile_picture_payload(user_id=user_id, user_item=user_item)
        try:
            result = _require_update_response(
                await client.users.update_user(user_id=user_id, user=payload, timeout=timeout)
            )
        except (AttributeError, TypeError, ValueError):
            try:
                result = await client.request(
                    "POST",
                    _DIRECT_USER_ROUTE,
                    path_params={"user_id": user_id},
                    json=payload,
                    timeout=timeout,
                )
                result = _require_update_response(result)
            except (TypeError, ValueError):
                result = await client.users.update_user.raw(
                    user_id=user_id,
                    user=payload,
                    timeout=timeout,
                )
        if wait_for_consistency:
            await _wait_for_profile_photo_state_async(
                client,
                user_id=user_id,
                timeout=timeout,
                consistency_timeout=consistency_timeout,
                consistency_poll_interval=consistency_poll_interval,
                predicate=lambda photo_id: photo_id is None,
                expectation="PhotoId to become None after profile-picture removal",
            )
        return result
    except (AttributeError, TypeError, ValueError):
        raw_response = await client.users.get_user.raw(user_id=user_id, timeout=timeout)
        user_item = _extract_user_item(raw_response)
        payload = _build_remove_profile_picture_payload(user_id=user_id, user_item=user_item)
        result = await client.users.update_user.raw(user_id=user_id, user=payload, timeout=timeout)
        if wait_for_consistency:
            await _wait_for_profile_photo_state_async(
                client,
                user_id=user_id,
                timeout=timeout,
                consistency_timeout=consistency_timeout,
                consistency_poll_interval=consistency_poll_interval,
                predicate=lambda photo_id: photo_id is None,
                expectation="PhotoId to become None after profile-picture removal",
            )
        return result
