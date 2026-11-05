"""HTTP DTOs owned by the FastAPI boundary."""

from typing import Annotated, Literal

from pydantic import BaseModel, StringConstraints, field_validator

NonEmptyPerson = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class HealthResponse(BaseModel):
    """Response returned by the health endpoint."""

    status: Literal["ok"]


class RecordKarmaRequest(BaseModel):
    """Request DTO for recording a Karma adjustment."""

    person: NonEmptyPerson
    points: int

    @field_validator("points")
    @classmethod
    def reject_zero_points(cls, value: int) -> int:
        """Reject an adjustment that would not change Karma."""
        if value == 0:
            msg = "Karma points cannot be zero."
            raise ValueError(msg)
        return value


class RecordedKarmaResponse(BaseModel):
    """Response DTO for an accepted Karma adjustment."""

    person: str
    points: int


class KarmaStateResponse(BaseModel):
    """Response DTO for the current UTC-day Karma state."""

    person: str
    adjustments: list[int]
    daily_balance: int
