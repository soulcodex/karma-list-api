"""Karma concepts and in-memory state used by the workshop service."""

from dataclasses import dataclass, field
from datetime import UTC, date, datetime


@dataclass(frozen=True)
class PersonName:
    """A validated recipient of a Karma adjustment."""

    value: str

    def __post_init__(self) -> None:
        """Reject a name that carries no meaning."""
        if not self.value.strip():
            msg = "A person name cannot be blank."
            raise ValueError(msg)


@dataclass(frozen=True)
class KarmaPoints:
    """A non-zero Karma adjustment."""

    value: int

    def __post_init__(self) -> None:
        """Reject an adjustment that changes nothing."""
        if self.value == 0:
            msg = "Karma points cannot be zero."
            raise ValueError(msg)


@dataclass(frozen=True)
class KarmaAdjustment:
    """One recorded Karma adjustment."""

    person: PersonName
    points: KarmaPoints
    recorded_at: datetime


def empty_adjustments() -> list[KarmaAdjustment]:
    """Create the mutable list owned by one in-memory ledger."""
    return []


@dataclass
class InMemoryKarmaLedger:
    """Stores workshop adjustments until the service restarts."""

    _adjustments: list[KarmaAdjustment] = field(default_factory=empty_adjustments)

    def record(self, adjustment: KarmaAdjustment) -> None:
        """Store one accepted adjustment."""
        self._adjustments.append(adjustment)

    def daily_adjustments_for(self, person: PersonName, day: date) -> tuple[KarmaAdjustment, ...]:
        """Return one person's adjustments recorded on the given UTC date."""
        return tuple(
            adjustment
            for adjustment in self._adjustments
            if adjustment.person == person and adjustment.recorded_at.date() == day
        )


def utc_now() -> datetime:
    """Return the current instant in UTC."""
    return datetime.now(UTC)
