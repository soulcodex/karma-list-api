# Karma API

Companion Python repository for **The Agent Is Not the System** workshop.

It provides a small functional FastAPI service for one focused workshop change. It is not a
production-ready service.

## Workshop tasks

The primary outcome is a configurable, portable router. Karma API is the small service used to
validate its guidance.

- [ ] Establish a factual baseline of the Karma API and its current constraints.
- [ ] Capture an unrouted baseline answer about the service.
- [ ] Add evidence and planning rows to the portable router, then compare fresh-session output.
- [ ] Add anti-slop guidance and compare the same handoff prompt.
- [ ] Add Python and transversal guidance before changing the daily Karma budget.
- [ ] Write business tests, implement the daily limits, and run deterministic checks.
- [ ] Add review guidance and challenge the result from a fresh context.

The portable router belongs in the companion harness repository. This repository supplies the
project instructions, working happy path, and the daily-budget exercise.

## Setup

```bash
uv sync
uv run uvicorn karma.app:app --reload
```

The baseline exposes `GET /health`, `POST /karma`, and `GET /karma/{person}`. It records non-zero
adjustments in memory and returns the current UTC-day state. It intentionally does not enforce the
daily `+5` and `-5` budgets. The feature contract lives in `docs/context/karma/INDEX.md`.

## Checks

```bash
uv run rumdl fmt --check --deny-config-warnings .
uv run rumdl check --deny-config-warnings .
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pylint src tools
uv run pytest
uv run python tools/check_type_boundaries.py src
```

Format Markdown with `uv run rumdl fmt .`.
