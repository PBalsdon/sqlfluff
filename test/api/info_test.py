"""Test using sqlfluff to extract elements of queries."""

import sqlfluff
from sqlfluff.core.linter import RuleTuple


def test__api__info_dialects():
    """Basic linting of dialects."""
    dialects = sqlfluff.list_dialects()
    assert isinstance(dialects, list)
    assert ("ansi", "ansi", "nothing") in dialects


def test__api__info_rules():
    """Basic linting of dialects."""
    rules = sqlfluff.list_rules()
    assert isinstance(rules, list)
    assert (
        RuleTuple(
            code="LT01",
            name="layout.spacing",
            description="Unnecessary whitespace.",
            groups=("all", "core", "layout"),
            aliases=("L001", "L039"),
        )
        in rules
    )
