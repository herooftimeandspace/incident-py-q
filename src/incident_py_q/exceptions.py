"""Package-specific exception types."""

from __future__ import annotations


class IncidentIQError(Exception):
    """Base exception for non-HTTP SDK errors."""


class ConfigurationError(IncidentIQError):
    """Raised when required runtime configuration is missing or invalid."""


class SchemaValidationError(ValueError, IncidentIQError):
    """Raised when a payload violates the bundled API response schema."""

