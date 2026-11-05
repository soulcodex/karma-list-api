from typing import Protocol, cast

from fastapi.testclient import TestClient
from httpx2 import Response

from karma.app import create_app


class HttpClient(Protocol):
    """The HTTP behavior exercised by the workshop contract tests."""

    def get(self, url: str) -> Response:
        """Perform one HTTP GET request."""
        ...

    def post(self, url: str, json: object) -> Response:
        """Perform one HTTP POST request."""
        ...


def test_records_an_adjustment_and_returns_current_daily_state() -> None:
    client = cast(HttpClient, TestClient(create_app()))

    recorded = client.post("/karma", json={"person": "Ada", "points": 2})
    state = client.get("/karma/Ada")

    assert recorded.status_code == 201
    assert recorded.json() == {"person": "Ada", "points": 2}
    assert state.status_code == 200
    assert state.json() == {"person": "Ada", "adjustments": [2], "daily_balance": 2}
