from __future__ import annotations

import pytest


def pytest_assertrepr_compare(
    config: pytest.Config, op: str, left: object, right: object
) -> list[str] | None:
    from tests.utils import ExpectedDict

    if isinstance(right, ExpectedDict) and op == "==":
        return ["dictionary matches expectation"] + right.errors

    return None
