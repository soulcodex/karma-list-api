# Karma API

Companion Python repository for **The Agent Is Not the System** workshop.

It starts as a small FastAPI service and evolves into a functional Karma API through the workshop
prompts. It is not a production-ready service.

## Setup

```bash
uv sync
uv run uvicorn karma.app:app --reload
```

The starter exposes `GET /health`. The Karma feature contract lives in
`docs/context/karma/INDEX.md`.

## Checks

```bash
uv run rumdl fmt --check --deny-config-warnings .
uv run rumdl check --deny-config-warnings .
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pylint src
uv run pytest
```

Format Markdown with `uv run rumdl fmt .`.
