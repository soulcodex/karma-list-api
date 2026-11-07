"""FastAPI entry point for the workshop service."""

from fastapi import FastAPI

from karma.contracts import HealthResponse


def create_app() -> FastAPI:
    """Build the health-only workshop baseline."""
    application = FastAPI(title="Karma API")

    @application.get("/health")
    def health() -> HealthResponse:
        """Report that the workshop service is running."""
        return HealthResponse(status="ok")

    return application


app = create_app()
