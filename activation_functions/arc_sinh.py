from math import asinh, sqrt


def f(x: float) -> float:
    return asinh(x)


def df(x: float) -> float:
    return 1/sqrt(x**2+1)
