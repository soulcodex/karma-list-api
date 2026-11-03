# Karma List API

## Always-on contract

- Keep the service small and functional. Do not add production concerns that the current feature does not require.
- Establish facts from code, tests, configuration, or an authoritative source before making a material claim or design decision.
- Prefer concise outputs that state the result, evidence, and next action.
- Preserve existing project constraints. Do not treat an instruction as evidence that an implementation behaves as described.

## Lazy router

- Before changing Python code, tests, or type configuration, read `docs/CODE_STYLE_GUIDES.md`.
- Before changing boundaries, persistence, dependencies, or package structure, read `docs/ARCHITECTURE.md`.
- Before changing Karma behavior, API contracts, or business tests, read `docs/context/karma/INDEX.md`.
- Do not preload every document. Read only the guidance that the current task needs.

## Verification

- Run the narrowest relevant deterministic checks after a change.
- Business tests must show an observable Karma rule or a credible regression.
- Formatting, linting, type checking, and module-size checks support review. They do not prove business behavior.
