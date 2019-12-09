from math import sqrt


def f(x: float) -> float:
    return (sqrt(x**2 + 1) - 1)/2 + x


def df(x: float) -> float:
    return x/(2*sqrt(x**2 + 1)) + 1
