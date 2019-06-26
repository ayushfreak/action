from typing import List, Iterable


# same-line ignore
def first() -> int:
    return "string"  # pyre-ignore


# previous-line ignore
def second() -> int:
    print("ayush")
    # pyre-ignore
    return "ayush"


def third() -> int:
    return "string"  # pyre-fixme


def fourth() -> int:
    return "string"  # type: ignore


# only ignore return errors
def fifth() -> int:
    return "ayush"  # pyre-ignore[7]


def to_seconds(milliseconds: Iterable[float]) -> List[int]:
    return [int(x/1000.0) for x in milliseconds]


my_list: List[int] = [1]
my_list = to_seconds(my_list)