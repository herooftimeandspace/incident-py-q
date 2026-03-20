"""Tests for internal utility helpers."""

from __future__ import annotations

import pytest

from incident_py_q._utils import render_path, to_snake_case


def test_to_snake_case_normalizes_common_shapes() -> None:
    assert to_snake_case("ThingId") == "thing_id"
    assert to_snake_case("pageSize") == "page_size"
    assert to_snake_case("custom-field name") == "custom_field_name"
    assert to_snake_case("$p") == "p"
    assert to_snake_case("123name") == "n_123name"
    assert to_snake_case("class") == "class_"


def test_to_snake_case_falls_back_for_empty_like_values() -> None:
    assert to_snake_case("") == "value"
    assert to_snake_case("$$$") == "value"


def test_render_path_substitutes_and_escapes() -> None:
    rendered = render_path("/things/{ThingId}", {"ThingId": "abc/123"})
    assert rendered == "/things/abc%2F123"


def test_render_path_requires_all_placeholders() -> None:
    with pytest.raises(ValueError):
        render_path("/things/{ThingId}", None)
    with pytest.raises(ValueError):
        render_path("/things/{ThingId}/{PartId}", {"ThingId": "a"})
