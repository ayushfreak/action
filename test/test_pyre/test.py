
from typing import Any

a = 5
def foo() -> int:
    return test(123)  # type error: expected `int` but got `Any`

if 1===:
    print("will not work")

def test(num: int) -> Any:
    print(num)
    return "ayush"

#
# def test(num: int) -> str:
#     print(num)
#     return "ayush"
