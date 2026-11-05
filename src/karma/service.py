"""Application operations for the Karma API."""

from dataclasses import dataclass
from datetime import datetime

from karma.domain import InMemoryKarmaLedger, KarmaAdjustment, KarmaPoints, PersonName


@dataclass(frozen=True)
class RecordKarmaAdjustment:
    """The typed input for recording one adjustment."""

    person: PersonName
    points: KarmaPoints


@dataclass(frozen=True)
class DailyKarmaState:
    """One person's adjustments and current UTC-day balance."""

    person: PersonName
    adjustments: tuple[KarmaAdjustment, ...]

    @property
    def daily_balance(self) -> int:
        """Sum the points recorded for the represented day."""
        return sum(adjustment.points.value for adjustment in self.adjustments)


@dataclass
class KarmaService:
    """Coordinates the in-memory ledger without owning HTTP concerns."""

    ledger: InMemoryKarmaLedger

    def record(self, command: RecordKarmaAdjustment, now: datetime) -> KarmaAdjustment:
        """Record a valid adjustment without applying the workshop's daily budget yet."""
        adjustment = KarmaAdjustment(
            person=command.person,
            points=command.points,
            recorded_at=now,
        )
        self.ledger.record(adjustment)
        return adjustment

    def daily_state(self, person: PersonName, now: datetime) -> DailyKarmaState:
        """Return the person's adjustments for the current UTC date."""
        return DailyKarmaState(
            person=person,
            adjustments=self.ledger.daily_adjustments_for(person, now.date()),
        )
