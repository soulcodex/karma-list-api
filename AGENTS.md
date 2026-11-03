# Karma API

## Always-on contract

- Keep the service small and functional. Do not add production concerns that the current feature
  does not require.
- Establish facts from code, tests, configuration, or an authoritative source before making a
  material claim or design decision.
- Prefer concise outputs that state the result, evidence, and next action.
- Preserve existing project constraints. Do not treat an instruction as evidence that an
  implementation behaves as described.

## Lazy context router

Read the source before taking the matching action. Load only the rows the task needs.

| Source                        | Read when                                                                                 | What it governs                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `docs/CODE_STYLE_GUIDES.md`   | Changing Python code, tests, type configuration, or module structure.                     | Typed boundaries, domain isolation, test quality, and the module-size signal.   |
| `docs/ARCHITECTURE.md`        | Changing boundaries, persistence, dependencies, package structure, or adapter direction.  | The HTTP edge, Karma domain, storage boundary, and explicit exclusions.         |
| `docs/context/karma/INDEX.md` | Changing Karma behavior, API contracts, request models, domain policy, or business tests. | The goal, vocabulary, invariants, HTTP contract, time semantics, and non-goals. |

Do not preload every document. Read the smallest applicable context before planning or editing.

## Verification

- Run the narrowest relevant deterministic checks after a change.
- Business tests must show an observable Karma rule or a credible regression.
- Formatting, linting, type checking, and module-size checks support review. They do not prove
  business behavior.
- Run `uv run rumdl fmt --check --deny-config-warnings .` and
  `uv run rumdl check --deny-config-warnings .` after changing Markdown.
- Run `uv run python tools/check_type_boundaries.py src` after changing Python signatures.
