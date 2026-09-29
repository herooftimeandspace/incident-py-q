"""Incident IQ API client and dynamic SDK.

This package provides:

- A low-level HTTP client for Incident IQ (`Client` and `AsyncClient`)
- Runtime response validation against bundled schema contracts
- A dynamic SDK generated from bundled Incident IQ API contracts
- Deprecated aliases for method names that predate the Golden OpenAPI migration
  (`legacy_alias_conflicts` reports the names that could not be preserved)
"""

from .client import AsyncClient, Client
from .compat import DeprecatedMethodAlias, legacy_alias_conflicts
from .version import __version__

__all__ = [
    "AsyncClient",
    "Client",
    "DeprecatedMethodAlias",
    "__version__",
    "legacy_alias_conflicts",
]
