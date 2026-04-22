"""PNG normalization helpers for image uploads."""

from __future__ import annotations

import math
from io import BytesIO
from os import PathLike
from pathlib import Path

from PIL import Image, UnidentifiedImageError

MAX_PNG_UPLOAD_BYTES = 1_048_576
_RESIZE_SAFETY_FACTOR = 0.95
_MAX_RESIZE_RATIO = 0.9


def prepare_png_upload(
    source: str | PathLike[str],
    *,
    max_bytes: int = MAX_PNG_UPLOAD_BYTES,
) -> tuple[str, bytes, str]:
    """Convert an input image to a size-limited PNG upload payload."""
    path = Path(source)
    try:
        with Image.open(path) as image:
            image.load()
            normalized = _normalize_image_mode(image)
    except FileNotFoundError:
        raise
    except UnidentifiedImageError as exc:
        raise ValueError(f"Profile picture upload requires an image file, got {path.name!r}.") from exc
    except OSError as exc:
        raise ValueError(f"Could not read image data from {path.name!r}.") from exc

    payload = _encode_png_under_limit(normalized, max_bytes=max_bytes)
    filename = f"{path.stem}.png"
    return filename, payload, "image/png"


def _normalize_image_mode(image: Image.Image) -> Image.Image:
    if image.mode in {"RGB", "RGBA", "L", "LA"}:
        return image.copy()
    if image.mode == "P":
        target_mode = "RGBA" if "transparency" in image.info else "RGB"
        return image.convert(target_mode)
    target_mode = "RGBA" if "transparency" in image.info else "RGB"
    return image.convert(target_mode)


def _encode_png_under_limit(image: Image.Image, *, max_bytes: int) -> bytes:
    current = image
    while True:
        payload = _encode_png(current)
        if len(payload) <= max_bytes:
            return payload

        width, height = current.size
        if width <= 1 and height <= 1:
            raise ValueError(
                f"Profile picture PNG output could not be reduced below {max_bytes} bytes."
            )

        scale = min(
            _MAX_RESIZE_RATIO,
            math.sqrt(max_bytes / len(payload)) * _RESIZE_SAFETY_FACTOR,
        )
        new_width = max(1, int(width * scale))
        new_height = max(1, int(height * scale))
        if (new_width, new_height) == current.size:
            new_width = max(1, width - 1)
            new_height = max(1, height - 1)
        current = current.resize((new_width, new_height), Image.Resampling.LANCZOS)


def _encode_png(image: Image.Image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()
