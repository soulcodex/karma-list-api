from typing import Protocol, cast

from fastapi.testclient import TestClient
from httpx import Response

from karma_list.app import app


class HttpClient(Protocol):
    def get(self, url: str) -> Response: ...


def test_health_reports_service_status() -> None:
    client = cast(HttpClient, TestClient(app))
    response = client.get("/health")
    payload = cast(dict[str, str], response.json())

    assert response.status_code == 200
    assert payload == {"status": "ok"}
