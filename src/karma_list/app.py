"""FastAPI entry point for the workshop service."""

from fastapi import FastAPI

app = FastAPI(title="Karma List API")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the workshop service is running."""
    return {"status": "ok"}
