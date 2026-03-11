"""Incident IQ API client and dynamic SDK.

This package provides:

- A low-level HTTP client for Incident IQ (`Client` and `AsyncClient`)
- Runtime response validation against bundled schema contracts
- A dynamic SDK generated from bundled Incident IQ API contracts
"""

from .client import AsyncClient, Client
from .version import __version__

__all__ = ["AsyncClient", "Client", "__version__"]
