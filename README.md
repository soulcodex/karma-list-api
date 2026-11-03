# Karma API

Companion Python repository for **The Agent Is Not the System** workshop.

It starts as a small FastAPI service and evolves into a functional Karma API through the workshop
prompts. It is not a production-ready service.

## Workshop tasks

The primary outcome is a configurable, portable harness. Karma API is the small service used to
validate it.

- [ ] Establish a factual baseline of the Karma API and its current constraints.
- [ ] Create a portable harness kernel with a root `AGENTS.md`, lazy context routing, transversal
  rules, architecture guidance, and skills or agent definitions.
- [ ] Configure the kernel for the chosen host: OpenCode, Codex, or Pi.
- [ ] Give the agent a small, evidence-based feature task and require concise reporting of evidence,
  changes, and verification.
- [ ] Add deterministic quality gates that the agent cannot negotiate away.
- [ ] Implement the Karma API slice with typed boundaries, value objects, business-rule tests, and
  in-memory persistence.
- [ ] Introduce a realistic bad change or incomplete solution and use the harness plus deterministic
  checks to reject it.
- [ ] Refine the harness from that evidence, then rerun the relevant task.
- [ ] Leave with a portable kernel that can be adapted to another supported coding agent.

Each attendee fully configures and validates one chosen host. The portable kernel and thin host
adapter model make the harness transferable without requiring three integrations during the
workshop.

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
uv run pylint src tools
uv run pytest
uv run python tools/check_type_boundaries.py src
```

Format Markdown with `uv run rumdl fmt .`.
