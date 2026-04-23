"""Tests for the explicit Silver runtime surface."""

from __future__ import annotations

import asyncio
import struct
from io import BytesIO
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import httpx
import pytest
import respx
from PIL import Image

from incident_py_q import AsyncClient, Client
from incident_py_q.media import prepare_png_upload
from incident_py_q.schema.registry import SchemaRegistry
from incident_py_q.silver.inventory import SilverMethodMetadata, SilverParameterMetadata


def _stub_silver_metadata() -> tuple[SilverMethodMetadata, ...]:
    return (
        SilverMethodMetadata(
            namespace_path=("analytics",),
            method_name="get_agent_current_stats",
            http_method="GET",
            route="/api/v1.0/analytics/agent-current-stats",
            parameters=(),
            summary="HAR-derived analytics stats route.",
            description="Silver route used for runtime testing.",
            typed_return="dict[str, Any] | list[Any] | None",
            raw_return="dict[str, Any] | list[Any] | None",
            sources=("unit-test.har",),
            status_codes=(200,),
            uses_app_headers=False,
        ),
        SilverMethodMetadata(
            namespace_path=("apps", "widgets"),
            method_name="get_widget",
            http_method="GET",
            route="/api/v1.0/apps/widgets/{widget_id}",
            parameters=(
                SilverParameterMetadata(
                    python_name="widget_id",
                    api_name="widget_id",
                    location="path",
                    required=True,
                    type_display="str",
                    description="Widget identifier.",
                ),
            ),
            summary="HAR-derived widget route.",
            description="Silver route used for runtime testing.",
            typed_return="dict[str, Any] | list[Any] | None",
            raw_return="dict[str, Any] | list[Any] | None",
            sources=("unit-test.har",),
            status_codes=(200,),
            uses_app_headers=True,
        ),
    )


def _write_test_image(
    path: Path,
    *,
    image_format: str,
    size: tuple[int, int] = (24, 24),
    color: tuple[int, int, int] = (12, 34, 56),
) -> None:
    Image.new("RGB", size, color=color).save(path, format=image_format)


def _extract_png_dimensions(payload: bytes) -> tuple[int, int]:
    signature = b"\x89PNG\r\n\x1a\n"
    start = payload.find(signature)
    if start < 0:
        raise AssertionError("multipart payload does not contain PNG bytes")
    return struct.unpack(">II", payload[start + 16 : start + 24])


class _ModelPayload:
    def __init__(self, payload: dict[str, Any]) -> None:
        self._payload = payload

    def model_dump(self, *, by_alias: bool = True) -> dict[str, Any]:
        return dict(self._payload)


class _FakeGetUser:
    def __init__(
        self,
        *,
        typed_result: Any = None,
        raw_result: Any = None,
        typed_exception: Exception | None = None,
    ) -> None:
        self.typed_result = typed_result
        self.raw_result = raw_result
        self.typed_exception = typed_exception
        self.calls: list[dict[str, Any]] = []
        self.raw_calls: list[dict[str, Any]] = []

    def __call__(self, **kwargs: Any) -> Any:
        self.calls.append(kwargs)
        if self.typed_exception is not None:
            raise self.typed_exception
        return self.typed_result

    def raw(self, **kwargs: Any) -> Any:
        self.raw_calls.append(kwargs)
        return self.raw_result


class _FakeUpdateUser:
    def __init__(
        self,
        *,
        typed_result: Any = None,
        raw_result: Any = None,
        typed_exception: Exception | None = None,
    ) -> None:
        self.typed_result = typed_result
        self.raw_result = raw_result
        self.typed_exception = typed_exception
        self.calls: list[dict[str, Any]] = []
        self.raw_calls: list[dict[str, Any]] = []

    def __call__(self, **kwargs: Any) -> Any:
        self.calls.append(kwargs)
        if self.typed_exception is not None:
            raise self.typed_exception
        return self.typed_result

    def raw(self, **kwargs: Any) -> Any:
        self.raw_calls.append(kwargs)
        return self.raw_result


class _RequestRecorder:
    def __init__(self, responses: list[Any] | None = None) -> None:
        self.responses = list(responses or [])
        self.calls: list[dict[str, Any]] = []

    def __call__(self, method: str, path: str, **kwargs: Any) -> Any:
        self.calls.append({"method": method, "path": path, **kwargs})
        if self.responses:
            return self.responses.pop(0)
        raise AssertionError(f"unexpected request call {method} {path}")


def _profile_picture_silver_metadata() -> tuple[SilverMethodMetadata, ...]:
    return (
        SilverMethodMetadata(
            namespace_path=("profiles",),
            method_name="post_profile_picture",
            http_method="POST",
            route="/api/v1.0/profiles/{user_id}/picture",
            parameters=(
                SilverParameterMetadata(
                    python_name="user_id",
                    api_name="user_id",
                    location="path",
                    required=True,
                    type_display="str",
                    description="User identifier.",
                ),
                SilverParameterMetadata(
                    python_name="file",
                    api_name="File",
                    location="file",
                    required=True,
                    type_display="str | PathLike[str]",
                    description="File to upload.",
                ),
            ),
            summary="HAR-derived profile picture upload route.",
            description="Silver route used for multipart runtime testing.",
            typed_return="dict[str, Any] | list[Any] | None",
            raw_return="dict[str, Any] | list[Any] | None",
            sources=("unit-test.har",),
            status_codes=(200,),
            uses_app_headers=False,
        ),
    )


def _full_user_item() -> dict[str, Any]:
    return {
        "UserId": "user-123",
        "IsDeleted": False,
        "SiteId": "site-1",
        "ProductId": "product-1",
        "CreatedDate": "2026-04-06T13:23:58.193",
        "ModifiedDate": "2026-04-22T17:24:53.283",
        "LocationId": "location-1",
        "IsActive": True,
        "IsOnline": False,
        "IsOnlineLastUpdated": "2026-04-22T17:24:53.283Z",
        "RoleId": "role-1",
        "AccountSetupProgress": 0,
        "TrainingPercentComplete": 0,
        "IsEmailVerified": False,
        "IsWelcomeEmailSent": True,
        "PreventProviderUpdates": False,
        "IsOutOfOffice": False,
        "Portal": 2,
        "UpdateCustomFields": False,
        "PhotoId": "photo-1",
        "FirstName": "Ada",
        "LastName": "Lovelace",
        "Options": {"Notifications": {"TicketUpdated": True}},
        "DataMappings": {"Name": None},
        "CustomFieldValues": [{"FieldId": "field-1"}],
    }


def _landscape_center_crop_source(path: Path, *, image_format: str) -> None:
    image = Image.new("RGB", (6, 4), color=(0, 255, 0))
    for x in range(1):
        for y in range(4):
            image.putpixel((x, y), (255, 0, 0))
    for x in range(5, 6):
        for y in range(4):
            image.putpixel((x, y), (0, 0, 255))
    image.save(path, format=image_format)


def _portrait_center_crop_source(path: Path, *, image_format: str) -> None:
    image = Image.new("RGB", (4, 6), color=(0, 255, 0))
    for y in range(1):
        for x in range(4):
            image.putpixel((x, y), (255, 0, 0))
    for y in range(5, 6):
        for x in range(4):
            image.putpixel((x, y), (0, 0, 255))
    image.save(path, format=image_format)


def _square_source_with_distinct_corners(path: Path, *, image_format: str) -> None:
    image = Image.new("RGB", (4, 4), color=(0, 255, 0))
    image.putpixel((0, 0), (255, 0, 0))
    image.putpixel((3, 3), (0, 0, 255))
    image.save(path, format=image_format)


@respx.mock
def test_client_exposes_explicit_silver_surface(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("incident_py_q.silver.runtime.build_silver_metadata", _stub_silver_metadata)
    respx.get("https://tenant.example/api/v1.0/analytics/agent-current-stats").mock(
        return_value=httpx.Response(200, json={"count": 1})
    )
    respx.get("https://tenant.example/api/v1.0/apps/widgets/widget-123").mock(
        return_value=httpx.Response(200, json={"widgetId": "widget-123"})
    )

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
        app_headers={"X-App-Token": "secret"},
    )
    try:
        assert client.apps is client.silver.apps
        assert client.silver.analytics.get_agent_current_stats() == {"count": 1}
        widgets: Any = client.silver.apps.widgets
        assert widgets.get_widget(widget_id="widget-123") == {
            "widgetId": "widget-123"
        }
        inventory = client.silver_sdk_inventory()
        assert {entry["namespace"] for entry in inventory} >= {"analytics", "apps.widgets", "apps.registry"}
    finally:
        client.close()


@pytest.mark.parametrize(
    ("extension", "image_format"),
    [
        ("jpg", "JPEG"),
        ("jpeg", "JPEG"),
        ("png", "PNG"),
        ("gif", "GIF"),
        ("webp", "WEBP"),
        ("bmp", "BMP"),
    ],
)
@respx.mock
def test_client_silver_profile_picture_upload_normalizes_common_formats_inside_method(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    extension: str,
    image_format: str,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        _profile_picture_silver_metadata,
    )
    route = respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    upload_path = tmp_path / f"avatar.{extension}"
    _write_test_image(upload_path, image_format=image_format, size=(48, 32))

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    try:
        assert client.silver.profiles.post_profile_picture(
            user_id="user-123",
            file=upload_path,
        ) == {"ok": True}
    finally:
        client.close()

    assert route.call_count == 1
    request = route.calls[0].request
    assert "multipart/form-data" in request.headers["content-type"]
    assert b'name="File"' in request.content
    assert b'filename="avatar.png"' in request.content
    assert b"image/png" in request.content
    assert _extract_png_dimensions(request.content) == (32, 32)


@respx.mock
def test_async_client_silver_profile_picture_upload_uses_multipart_file(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        _profile_picture_silver_metadata,
    )
    route = respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    upload_path = tmp_path / "avatar.jpg"
    _write_test_image(upload_path, image_format="JPEG")

    async def run() -> None:
        client = AsyncClient(
            base_url="https://tenant.example/api/v1",
            api_token="token-123",
            registry=tiny_registry,
        )
        try:
            assert await client.silver.profiles.post_profile_picture(
                user_id="user-123",
                file=upload_path,
            ) == {"ok": True}
        finally:
            await client.close()

    asyncio.run(run())

    assert route.call_count == 1
    request = route.calls[0].request
    assert "multipart/form-data" in request.headers["content-type"]
    assert b'name="File"' in request.content
    assert b'filename="avatar.png"' in request.content
    assert b"image/png" in request.content


@pytest.mark.parametrize(
    ("extension", "image_format"),
    [
        ("jpg", "JPEG"),
        ("jpeg", "JPEG"),
        ("png", "PNG"),
        ("gif", "GIF"),
        ("webp", "WEBP"),
        ("bmp", "BMP"),
    ],
)
def test_prepare_png_upload_normalizes_common_image_formats(
    tmp_path: Path,
    extension: str,
    image_format: str,
) -> None:
    upload_path = tmp_path / f"avatar.{extension}"
    _write_test_image(upload_path, image_format=image_format)

    filename, payload, content_type = prepare_png_upload(upload_path)

    assert filename == "avatar.png"
    assert content_type == "image/png"
    with Image.open(BytesIO(payload)) as image:
        assert image.format == "PNG"


def test_prepare_png_upload_preserves_square_images_when_square_crop_enabled(tmp_path: Path) -> None:
    upload_path = tmp_path / "square.png"
    _square_source_with_distinct_corners(upload_path, image_format="PNG")

    filename, payload, content_type = prepare_png_upload(upload_path, crop_to_square=True)

    assert filename == "square.png"
    assert content_type == "image/png"
    with Image.open(BytesIO(payload)) as image:
        assert image.size == (4, 4)
        assert image.getpixel((0, 0)) == (255, 0, 0)
        assert image.getpixel((3, 3)) == (0, 0, 255)


def test_prepare_png_upload_center_crops_landscape_images_when_square_crop_enabled(
    tmp_path: Path,
) -> None:
    upload_path = tmp_path / "landscape.png"
    _landscape_center_crop_source(upload_path, image_format="PNG")

    _, payload, _ = prepare_png_upload(upload_path, crop_to_square=True)

    with Image.open(BytesIO(payload)) as image:
        assert image.size == (4, 4)
        assert image.getpixel((0, 0)) == (0, 255, 0)
        assert image.getpixel((3, 3)) == (0, 255, 0)


def test_prepare_png_upload_center_crops_portrait_images_when_square_crop_enabled(
    tmp_path: Path,
) -> None:
    upload_path = tmp_path / "portrait.png"
    _portrait_center_crop_source(upload_path, image_format="PNG")

    _, payload, _ = prepare_png_upload(upload_path, crop_to_square=True)

    with Image.open(BytesIO(payload)) as image:
        assert image.size == (4, 4)
        assert image.getpixel((0, 0)) == (0, 255, 0)
        assert image.getpixel((3, 3)) == (0, 255, 0)


def test_prepare_png_upload_downscales_large_images(tmp_path: Path) -> None:
    upload_path = tmp_path / "oversized.png"
    Image.effect_noise((1024, 1024), 100).convert("L").save(upload_path, format="PNG")

    filename, payload, content_type = prepare_png_upload(upload_path, max_bytes=40_000)

    assert filename == "oversized.png"
    assert content_type == "image/png"
    assert len(payload) <= 40_000
    with Image.open(BytesIO(payload)) as image:
        assert image.format == "PNG"
        assert image.size[0] < 1024
        assert image.size[1] < 1024


def test_prepare_png_upload_rejects_non_images(tmp_path: Path) -> None:
    upload_path = tmp_path / "avatar.txt"
    upload_path.write_text("not-an-image", encoding="utf-8")

    with pytest.raises(ValueError, match="requires an image file"):
        prepare_png_upload(upload_path)


def test_prepare_png_upload_raises_for_missing_path(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        prepare_png_upload(tmp_path / "missing.png")


def test_client_silver_remove_profile_picture_uses_minimal_safe_payload(
    tiny_registry: SchemaRegistry,
) -> None:
    user_item = _full_user_item()
    get_user = _FakeGetUser(typed_result=_ModelPayload({"Item": dict(user_item)}))
    update_user = _FakeUpdateUser(typed_result={"updated": True})

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=get_user, update_user=update_user)
    client.request = _RequestRecorder()
    try:
        assert client.silver.profiles.remove_profile_picture(user_id="user-123") == {"updated": True}
    finally:
        client.close()

    assert get_user.raw_calls == []
    assert update_user.raw_calls == []
    assert len(update_user.calls) == 1

    update_call = update_user.calls[0]
    assert update_call["user_id"] == "user-123"
    payload = update_call["user"]
    expected_keys = {
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
        "PhotoId",
    }
    assert set(payload) == expected_keys
    assert payload["PhotoId"] is None
    for key in expected_keys - {"PhotoId"}:
        assert payload[key] == user_item[key]
    assert "FirstName" not in payload
    assert "LastName" not in payload
    assert "Options" not in payload
    assert "DataMappings" not in payload
    assert "CustomFieldValues" not in payload
    assert user_item["PhotoId"] == "photo-1"


def test_client_silver_remove_profile_picture_falls_back_to_raw_only_after_typed_failure(
    tiny_registry: SchemaRegistry,
) -> None:
    user_item = _full_user_item()
    get_user = _FakeGetUser(typed_exception=ValueError("typed route failed"), raw_result={"Item": dict(user_item)})
    update_user = _FakeUpdateUser(raw_result={"updated": True})
    request = _RequestRecorder(responses=["not-json", "not-json"])

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=get_user, update_user=update_user)
    client.request = request
    try:
        assert client.silver.profiles.remove_profile_picture(user_id="user-123") == {"updated": True}
    finally:
        client.close()

    assert len(get_user.calls) == 1
    assert len(request.calls) == 2
    assert len(get_user.raw_calls) == 1
    assert len(update_user.calls) == 1
    assert len(update_user.raw_calls) == 1


def test_async_client_silver_remove_profile_picture_uses_minimal_safe_payload(
    tiny_registry: SchemaRegistry,
) -> None:
    user_item = _full_user_item()

    class _AsyncFakeGetUser(_FakeGetUser):
        async def __call__(self, **kwargs: Any) -> Any:
            return super().__call__(**kwargs)

        async def raw(self, **kwargs: Any) -> Any:
            return super().raw(**kwargs)

    class _AsyncFakeUpdateUser(_FakeUpdateUser):
        async def __call__(self, **kwargs: Any) -> Any:
            return super().__call__(**kwargs)

        async def raw(self, **kwargs: Any) -> Any:
            return super().raw(**kwargs)

    async def run() -> None:
        get_user = _AsyncFakeGetUser(typed_result=_ModelPayload({"Item": dict(user_item)}))
        update_user = _AsyncFakeUpdateUser(typed_result={"updated": True})

        client = AsyncClient(
            base_url="https://tenant.example/api/v1",
            api_token="token-123",
            registry=tiny_registry,
        )
        client.users = SimpleNamespace(get_user=get_user, update_user=update_user)
        client.request = _RequestRecorder()
        try:
            assert await client.silver.profiles.remove_profile_picture(user_id="user-123") == {
                "updated": True
            }
        finally:
            await client.close()

        assert get_user.raw_calls == []
        assert update_user.raw_calls == []
        assert len(update_user.calls) == 1
        payload = update_user.calls[0]["user"]
        assert payload["PhotoId"] is None
        assert payload["RoleId"] == user_item["RoleId"]

    asyncio.run(run())


def test_client_silver_remove_profile_picture_falls_back_to_direct_json_route_when_typed_getter_returns_none(
    tiny_registry: SchemaRegistry,
) -> None:
    user_item = _full_user_item()
    get_user = _FakeGetUser(typed_result=None, raw_result={"Item": {"UserId": "wrong"}})
    update_user = _FakeUpdateUser(typed_exception=ValueError("typed update failed"))
    request = _RequestRecorder(
        responses=[
            {"Item": {**{k: v for k, v in user_item.items() if k not in {"ProductId", "TrainingPercentComplete", "UpdateCustomFields"}}, "Site": {"ProductId": user_item["ProductId"]}}},
            {"updated": True},
        ]
    )

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=get_user, update_user=update_user)
    client.request = request
    try:
        assert client.silver.profiles.remove_profile_picture(user_id="user-123") == {"updated": True}
    finally:
        client.close()

    assert len(get_user.calls) == 1
    assert get_user.raw_calls == []
    assert len(update_user.calls) == 1
    assert len(request.calls) == 2
    assert request.calls[0]["method"] == "GET"
    assert request.calls[0]["path"] == "/api/v1.0/users/{user_id}"
    assert request.calls[1]["method"] == "POST"
    payload = request.calls[1]["json"]
    assert payload["ProductId"] == user_item["ProductId"]
    assert payload["TrainingPercentComplete"] == 0
    assert payload["UpdateCustomFields"] is False
    assert payload["PhotoId"] is None
    assert "FirstName" not in payload


def test_client_silver_remove_profile_picture_waits_for_photo_id_to_clear(
    tiny_registry: SchemaRegistry,
) -> None:
    user_item = _full_user_item()
    get_user = _FakeGetUser(typed_result=None)
    update_user = _FakeUpdateUser(typed_result={"updated": True})
    request = _RequestRecorder(
        responses=[
            {"Item": dict(user_item)},
            {"Item": {**user_item, "PhotoId": "photo-1"}},
            {"Item": {**user_item, "PhotoId": None}},
        ]
    )

    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=get_user, update_user=update_user)
    client.request = request
    try:
        assert client.silver.profiles.remove_profile_picture(
            user_id="user-123",
            wait_for_consistency=True,
            consistency_timeout=0.01,
            consistency_poll_interval=0.0,
        ) == {"updated": True}
    finally:
        client.close()

    assert len(request.calls) == 3


@respx.mock
def test_client_silver_profile_picture_upload_waits_for_expected_file_id(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        _profile_picture_silver_metadata,
    )
    upload_path = tmp_path / "avatar.jpg"
    _write_test_image(upload_path, image_format="JPEG", size=(48, 32))
    route = respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"Item": {"FileId": "photo-2"}})
    )
    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=_FakeGetUser(typed_result=None))
    request = _RequestRecorder(
        responses=[
            {"Item": {**_full_user_item(), "PhotoId": "photo-1"}},
            {"Item": {**_full_user_item(), "PhotoId": "photo-1"}},
            {"Item": {**_full_user_item(), "PhotoId": "photo-2"}},
        ]
    )
    client.request = request
    try:
        assert client.silver.profiles.post_profile_picture(
            user_id="user-123",
            file=upload_path,
            wait_for_consistency=True,
            consistency_timeout=0.01,
            consistency_poll_interval=0.0,
        ) == {"Item": {"FileId": "photo-2"}}
    finally:
        client.close()

    assert route.call_count == 1
    assert [call["method"] for call in request.calls] == ["GET", "GET", "GET"]


@respx.mock
def test_client_silver_profile_picture_upload_waits_for_changed_photo_id_when_response_has_no_file_id(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        _profile_picture_silver_metadata,
    )
    upload_path = tmp_path / "avatar.jpg"
    _write_test_image(upload_path, image_format="JPEG")
    respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=_FakeGetUser(typed_result=None))
    request = _RequestRecorder(
        responses=[
            {"Item": {**_full_user_item(), "PhotoId": "photo-1"}},
            {"Item": {**_full_user_item(), "PhotoId": "photo-1"}},
            {"Item": {**_full_user_item(), "PhotoId": "photo-9"}},
        ]
    )
    client.request = request
    try:
        assert client.silver.profiles.post_profile_picture(
            user_id="user-123",
            file=upload_path,
            wait_for_consistency=True,
            consistency_timeout=0.01,
            consistency_poll_interval=0.0,
        ) == {"ok": True}
    finally:
        client.close()


@respx.mock
def test_client_silver_profile_picture_upload_raises_timeout_when_photo_id_does_not_converge(
    tiny_registry: SchemaRegistry,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "incident_py_q.silver.runtime.build_silver_metadata",
        _profile_picture_silver_metadata,
    )
    upload_path = tmp_path / "avatar.jpg"
    _write_test_image(upload_path, image_format="JPEG")
    respx.post("https://tenant.example/api/v1.0/profiles/user-123/picture").mock(
        return_value=httpx.Response(200, json={"Item": {"FileId": "photo-2"}})
    )
    client = Client(
        base_url="https://tenant.example/api/v1",
        api_token="token-123",
        registry=tiny_registry,
    )
    client.users = SimpleNamespace(get_user=_FakeGetUser(typed_result=None))
    request = _RequestRecorder(
        responses=[
            {"Item": {**_full_user_item(), "PhotoId": "photo-1"}},
            {"Item": {**_full_user_item(), "PhotoId": "photo-1"}},
        ]
    )
    client.request = request
    try:
        with pytest.raises(TimeoutError, match="did not converge"):
            client.silver.profiles.post_profile_picture(
                user_id="user-123",
                file=upload_path,
                wait_for_consistency=True,
                consistency_timeout=0.0,
                consistency_poll_interval=0.0,
            )
    finally:
        client.close()
