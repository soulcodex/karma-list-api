"""Regression tests for the type-boundary quality gate."""

from pathlib import Path

from tools.check_type_boundaries import find_violations


def write_source(tmp_path: Path, source: str) -> Path:
    """Write a temporary Python module for a boundary-check test."""
    path = tmp_path / "boundaries.py"
    path.write_text(source, encoding="utf-8")
    return path


def reported_function_names(violations: list[str]) -> set[str]:
    """Return the reported function names from checker output."""
    return {
        violation.split(" uses a mapping", maxsplit=1)[0].rsplit(": ", maxsplit=1)[-1]
        for violation in violations
    }


def test_rejects_unstructured_mapping_forms_at_function_boundaries(tmp_path: Path) -> None:
    """The gate finds direct, qualified, nested, and quoted mapping annotations."""
    path = write_source(
        tmp_path,
        """
import typing
from collections.abc import Mapping


def direct_input(payload: dict[str, int]) -> None:
    pass


def qualified_input(payload: typing.Dict[str, int]) -> None:
    pass


def nested_input(payload: dict[str, int] | None) -> None:
    pass


def quoted_input(payload: "dict[str, int]") -> None:
    pass


async def abstract_input(payload: Mapping[str, int]) -> None:
    pass


def direct_return() -> dict[str, int]:
    return {}


def qualified_return() -> typing.Dict[str, int]:
    return {}


def quoted_return() -> "Mapping[str, int]":
    return {}


async def nested_return() -> Mapping[str, int] | None:
    return None
""",
    )

    assert reported_function_names(find_violations(path)) == {
        "abstract_input",
        "direct_input",
        "direct_return",
        "nested_input",
        "nested_return",
        "qualified_input",
        "qualified_return",
        "quoted_input",
        "quoted_return",
    }


def test_allows_typed_boundaries_and_documented_exceptions(tmp_path: Path) -> None:
    """The gate keeps DTOs and an explicitly justified external contract valid."""
    path = write_source(
        tmp_path,
        """
class KarmaAdjustment:
    pass


class KarmaBalance:
    pass


def typed_boundary(payload: KarmaAdjustment) -> KarmaBalance:
    raise NotImplementedError


# plain-dict: Third-party callback contract.
def third_party_callback(payload: dict[str, str]) -> None:
    pass
""",
    )

    assert find_violations(path) == []
