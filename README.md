# Karma API

Companion Python repository for **The Agent Is Not the System** workshop. It starts as a
health-only FastAPI service. Attendees use their evolving harness to build the documented Karma API.
It is not a production-ready service.

## Workshop tasks

The primary outcome is a configurable, portable router. Karma API is the small service used to
validate its guidance.

- [ ] Establish a factual baseline of the health-only service and its target contract.
- [ ] Capture an unrouted baseline answer about the service.
- [ ] Add evidence and planning rows to the portable router, then compare fresh-session output.
- [ ] Add anti-slop guidance and compare the same handoff prompt.
- [ ] Add Python and transversal guidance before designing the first Karma API slice.
- [ ] Write focused contract tests, then implement the Karma endpoints and daily-budget policy.
- [ ] Add review guidance and challenge the result from a fresh context.

The portable router belongs in the companion harness repository. This repository supplies the
project instructions, working happy path, and the daily-budget exercise.

## Setup

```bash
uv sync
uv run uvicorn karma.app:app --reload
```

The baseline exposes only `GET /health`. The contract for `POST /karma` and
`GET /karma/{person_id}` lives in `docs/context/karma/INDEX.md`. It defines behavior and invariants,
not the implementation shape attendees must choose.

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
