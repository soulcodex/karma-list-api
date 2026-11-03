"""Reject unstructured mapping types at Python function boundaries."""

from __future__ import annotations

import ast
import sys
from collections.abc import Iterable
from pathlib import Path

MAPPING_TYPE_NAMES = frozenset({"dict", "Dict", "Mapping", "MutableMapping"})
JUSTIFICATION_PREFIX = "# plain-dict:"


def annotation_uses_mapping(annotation: ast.expr | None) -> bool:
    """Return whether an annotation includes an unstructured mapping type."""
    if annotation is None:
        return False

    for node in ast.walk(annotation):
        if isinstance(node, ast.Name) and node.id in MAPPING_TYPE_NAMES:
            return True
        if isinstance(node, ast.Attribute) and node.attr in MAPPING_TYPE_NAMES:
            return True
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            try:
                quoted_annotation = ast.parse(node.value, mode="eval").body
            except SyntaxError:
                continue
            if annotation_uses_mapping(quoted_annotation):
                return True

    return False


def function_annotations(node: ast.FunctionDef | ast.AsyncFunctionDef) -> Iterable[ast.expr]:
    """Yield annotated parameters and the return annotation for a function."""
    arguments = (*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs)
    if node.args.vararg is not None:
        arguments = (*arguments, node.args.vararg)
    if node.args.kwarg is not None:
        arguments = (*arguments, node.args.kwarg)

    for argument in arguments:
        if argument.annotation is not None:
            yield argument.annotation
    if node.returns is not None:
        yield node.returns


def has_justification(lines: list[str], line_number: int) -> bool:
    """Return whether the line immediately before a function justifies a mapping."""
    previous_line = line_number - 2
    return previous_line >= 0 and lines[previous_line].strip().startswith(JUSTIFICATION_PREFIX)


def find_violations(path: Path) -> list[str]:
    """Return unstructured mapping annotations without a durable justification."""
    source = path.read_text(encoding="utf-8")
    lines = source.splitlines()
    tree = ast.parse(source, filename=str(path))
    violations: list[str] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            continue
        if any(
            annotation_uses_mapping(annotation) for annotation in function_annotations(node)
        ) and not has_justification(lines, node.lineno):
            violations.append(
                f"{path}:{node.lineno}: {node.name} uses a mapping in its signature. "
                f"Use a DTO or add a preceding {JUSTIFICATION_PREFIX} reason."
            )

    return violations


def main() -> int:
    """Check every Python source file below the requested directory."""
    if len(sys.argv) != 2:
        print("Usage: check_type_boundaries.py <source-directory>")
        return 2

    source_directory = Path(sys.argv[1])
    violations = [
        violation
        for path in sorted(source_directory.rglob("*.py"))
        for violation in find_violations(path)
    ]
    if violations:
        print("\n".join(violations))
        return 1

    print("No unstructured mapping types found in Python function signatures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
