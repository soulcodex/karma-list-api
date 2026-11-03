"""FastAPI entry point for the workshop service."""

from fastapi import FastAPI

from karma.contracts import HealthResponse

app = FastAPI(title="Karma API")


@app.get("/health")
def health() -> HealthResponse:
    """Report that the workshop service is running."""
    return HealthResponse(status="ok")
