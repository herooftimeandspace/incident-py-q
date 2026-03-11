"""Live integration smoke tests (read-only) for Incident IQ tenant endpoints."""

from __future__ import annotations

import asyncio
import os
from typing import Any

import pytest

from incident_py_q import AsyncClient, Client


def _require_integration_env() -> None:
    required = ("INCIDENTIQ_TEST_BASE_URL", "INCIDENTIQ_TEST_API_TOKEN")
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        joined = ", ".join(missing)
        pytest.skip(f"Integration credentials not configured: missing {joined}")


@pytest.mark.integration
def test_sync_users_smoke() -> None:
    _require_integration_env()
    client = Client.from_test_env()
    try:
        payload: Any = client.users.get_users_legacy.raw()
    finally:
        client.close()
    assert payload is None or isinstance(payload, (dict, list))


@pytest.mark.integration
def test_async_users_smoke() -> None:
    _require_integration_env()
    client = AsyncClient.from_test_env()

    async def run() -> Any:
        try:
            return await client.users.get_users_legacy.raw()
        finally:
            await client.close()

    payload = asyncio.run(run())
    assert payload is None or isinstance(payload, (dict, list))
