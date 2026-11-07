# Code style guides

## Python boundaries

- Keep FastAPI request and response DTOs at the HTTP edge.
- Keep Karma policy in domain code that has no FastAPI or storage dependency.
- Use DTOs, value objects, and explicit domain types for every function input and output that
  carries structured data.
- Do not use `dict`, `Dict`, `Mapping`, or `MutableMapping` in a function signature by default. The
  repository check rejects them unless the immediately preceding line has a `# plain-dict:` comment
  that explains why a DTO or value object would be misleading.
- A justified plain dictionary still needs precise key and value types. It cannot use `Any` as a
  substitute for a DTO.
- Do not pass unstructured dictionaries through domain code.
- Introduce a value object only when it owns a validation rule or makes a domain operation clearer.
- Keep functions and modules cohesive. The 250-line module limit is a review signal, not an
  instruction to split related code mechanically.

## Tests

- Name tests after an observable rule or regression.
- Prefer direct domain tests for Karma policy and a small number of HTTP tests for the API contract.
- Do not add tests only to increase coverage.

## Verification pipeline

Choose the smallest section that covers the change. Run the complete pipeline before handing off a
cross-cutting change.

### Markdown

Run after changing Markdown. Format with `uv run rumdl fmt .` when required.

```bash
uv run rumdl fmt --check --deny-config-warnings .
uv run rumdl check --deny-config-warnings .
```

### Python source and tests

Run after changing Python source, tests, or type configuration.

```bash
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pylint src tools
```

Run this after changing a Python function signature. It rejects an unstructured mapping unless its
boundary has a justified exception.

```bash
uv run python tools/check_type_boundaries.py src
```

### Karma behavior

Run a focused test that proves the changed rule or regression. Run the full suite before a
cross-boundary handoff.

```bash
uv run pytest path/to/test.py -k rule_name
uv run pytest
```

## Output

- Show the commands run and whether they passed.
- Distinguish verified facts from design suggestions.
