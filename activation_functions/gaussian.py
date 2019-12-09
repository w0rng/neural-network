from math import exp


def f(x: float) -> float:
    return exp(-x**2)


def df(x: float) -> float:
    return -2*x*f(x)
