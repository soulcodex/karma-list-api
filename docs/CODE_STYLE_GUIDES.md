# Code style guides

## Python boundaries

- Keep FastAPI request and response models at the HTTP edge.
- Keep Karma policy in domain code that has no FastAPI or storage dependency.
- Use precise Python types. Do not pass unstructured dictionaries through domain code.
- Introduce a value object only when it owns a validation rule or makes a domain operation clearer.
- Keep functions and modules cohesive. The 250-line module limit is a review signal, not an instruction to split related code mechanically.

## Tests

- Name tests after an observable rule or regression.
- Prefer direct domain tests for Karma policy and a small number of HTTP tests for the API contract.
- Do not add tests only to increase coverage.

## Output

- Show the commands run and whether they passed.
- Distinguish verified facts from design suggestions.
