"""Internal utility helpers shared across modules."""

from __future__ import annotations

import keyword
import re
from urllib.parse import quote

_CAMEL_TO_SNAKE_RE = re.compile(r"(?<!^)(?=[A-Z])")
_NON_IDENTIFIER_RE = re.compile(r"[^0-9a-zA-Z_]")
_PATH_PARAM_RE = re.compile(r"\{([^}]+)\}")


def to_snake_case(value: str) -> str:
    """Convert common API-style names into Pythonic snake_case identifiers."""
    working = value.strip().replace("-", "_").replace(" ", "_").replace("$", "")
    if not working:
        return "value"
    if "_" not in working and any(ch.isupper() for ch in working):
        working = _CAMEL_TO_SNAKE_RE.sub("_", working)
    working = _NON_IDENTIFIER_RE.sub("_", working).strip("_").lower()
    if not working:
        return "value"
    if working[0].isdigit():
        working = f"n_{working}"
    if keyword.iskeyword(working):
        working = f"{working}_"
    return working


def render_path(path_template: str, path_params: dict[str, object] | None) -> str:
    """Render `{Param}` placeholders with URL-escaped values."""
    rendered = path_template
    placeholders = _PATH_PARAM_RE.findall(path_template)
    if placeholders:
        if not path_params:
            joined = ", ".join(sorted(placeholders))
            raise ValueError(f"Missing path parameters: {joined}")
        missing = [name for name in placeholders if name not in path_params]
        if missing:
            joined = ", ".join(sorted(missing))
            raise ValueError(f"Missing path parameters: {joined}")
    if not path_params:
        return rendered
    for key, value in path_params.items():
        rendered = rendered.replace(f"{{{key}}}", quote(str(value), safe=""))
    return rendered
