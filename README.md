# Karma API

Health-only FastAPI starter for **The Agent Is Not the System** workshop. Attendees use the companion
[harness workshop](https://github.com/soulcodex/agent-harness-workshop) to build the documented
Karma API. It is not a production-ready service.

## Setup

```bash
uv sync
uv run uvicorn karma.app:app --reload
```

The baseline exposes only `GET /health`. The contract for `POST /karma` and
`GET /karma/{person_id}` lives in `docs/context/karma/INDEX.md`. It defines behavior and invariants,
not the implementation shape attendees must choose.

The contract, architecture, and verification commands live in `docs/`.
