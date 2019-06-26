import typing
class C:
    a: int = 2

    def foo(self) -> str:
        return ""


A = typing.Union[int, str]
B = typing.Union[A, typing.List[str]]