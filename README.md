# Karma API

Health-only FastAPI starter for **The Agent Is Not the System** workshop. Use the companion
[harness workshop](https://github.com/soulcodex/agent-harness-workshop) to build and verify the
Karma API. It is not a production-ready service.

## Starting point

The baseline exposes only `GET /health`. You will build `POST /karma` and
`GET /karma/{person_id}` from the supplied contract. The contract defines behavior and invariants,
not the implementation shape.

## Before the workshop

Complete the isolated OpenCode setup in the harness repository first. Then install this project's
dependencies and optionally start the service:

```bash
uv sync
uv run uvicorn karma.app:app --reload
```

## Workshop route

1. Follow the harness [tasks](https://github.com/soulcodex/agent-harness-workshop/blob/main/WORKSHOP_TASKS.md)
   in order.
2. Copy one [prompt](https://github.com/soulcodex/agent-harness-workshop/blob/main/WORKSHOP_PROMPTS.md)
   at a time and open a fresh agent session after each router edit.
3. Use this repository to turn the supplied contract into tests and the smallest working service.

You are done when the Karma endpoints meet the contract, the daily directional budgets are enforced,
and focused business tests prove accepted and rejected behavior.

## Read when needed

| Need | Source |
| --- | --- |
| Product goal, API contract, and invariants | [Karma context](docs/context/karma/INDEX.md) |
| Boundaries and explicit exclusions | [Architecture](docs/ARCHITECTURE.md) |
| Types, tests, and verification commands | [Code style guide](docs/CODE_STYLE_GUIDES.md) |
| Local agent instructions | [AGENTS.md](AGENTS.md) |
