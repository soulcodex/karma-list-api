"""FastAPI entry point for the workshop service."""

from fastapi import FastAPI, status

from karma.contracts import (
    HealthResponse,
    KarmaStateResponse,
    RecordedKarmaResponse,
    RecordKarmaRequest,
)
from karma.domain import InMemoryKarmaLedger, KarmaPoints, PersonName, utc_now
from karma.service import KarmaService, RecordKarmaAdjustment


def create_app() -> FastAPI:
    """Build a small API with in-memory state for one process."""
    application = FastAPI(title="Karma API")
    service = KarmaService(ledger=InMemoryKarmaLedger())

    @application.get("/health")
    def health() -> HealthResponse:
        """Report that the workshop service is running."""
        return HealthResponse(status="ok")

    @application.post(
        "/karma", response_model=RecordedKarmaResponse, status_code=status.HTTP_201_CREATED
    )
    def record_karma(request: RecordKarmaRequest) -> RecordedKarmaResponse:
        """Record one valid, non-zero adjustment."""
        adjustment = service.record(
            RecordKarmaAdjustment(
                person=PersonName(request.person),
                points=KarmaPoints(request.points),
            ),
            now=utc_now(),
        )
        return RecordedKarmaResponse(
            person=adjustment.person.value,
            points=adjustment.points.value,
        )

    @application.get("/karma/{person}", response_model=KarmaStateResponse)
    def get_karma(person: str) -> KarmaStateResponse:
        """Return the named person's current UTC-day Karma state."""
        state = service.daily_state(PersonName(person), now=utc_now())
        return KarmaStateResponse(
            person=state.person.value,
            adjustments=[adjustment.points.value for adjustment in state.adjustments],
            daily_balance=state.daily_balance,
        )

    return application


app = create_app()
