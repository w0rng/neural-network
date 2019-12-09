from math import atan


def f(x: float) -> float:
    return atan(x)


def df(x: float) -> int:
    return 1/(x**2+1)
