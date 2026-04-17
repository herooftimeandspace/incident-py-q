"""Tests for the pdoc API docs generation script."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


def _load_generate_api_docs_module() -> ModuleType:
    script_path = Path("scripts/generate_api_docs.py")
    spec = importlib.util.spec_from_file_location("generate_api_docs_script", script_path)
    if spec is None or spec.loader is None:
        raise AssertionError("Unable to load scripts/generate_api_docs.py for testing.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sanitize_pdoc_html_rewrites_vscode_css_warnings(tmp_path: Path) -> None:
    module = _load_generate_api_docs_module()
    html_path = tmp_path / "incident_py_q.html"
    html_path.write_text(
        (
            "[type=button],[type=reset],[type=submit],button{-webkit-appearance:button}"
            "[type=search]{outline-offset:-2px;-webkit-appearance:textfield}"
            "::-webkit-search-decoration{-webkit-appearance:none}"
            "::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}"
            ".view-source-button{display:inline-block;float:right;font-size:.75rem;}"
        ),
        encoding="utf-8",
    )

    module._sanitize_pdoc_html(html_path)

    updated = html_path.read_text(encoding="utf-8")
    assert "appearance:button;-webkit-appearance:button" in updated
    assert "appearance:textfield;-webkit-appearance:textfield" in updated
    assert "appearance:none;-webkit-appearance:none" in updated
    assert ".view-source-button{float:right;font-size:.75rem;}" in updated
    assert "display:inline-block;float:right" not in updated

