
from typing import Any


def foo() -> int:
    return test(123)  # type error: expected `int` but got `Any`


def test(num: int) -> Any:
    print(num)
    return "ayush"

#
# def test(num: int) -> str:
#     print(num)
#     return "ayush"
