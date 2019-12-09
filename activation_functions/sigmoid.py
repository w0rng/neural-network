from math import exp as e


def f(x: float) -> float:
    return 1/(1+e(-x))


def df(x: float) -> int:
    return f(x)*(1-f(x))
