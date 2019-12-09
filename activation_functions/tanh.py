
from math import tanh


def f(x: float) -> float:
    return tanh(x)


def df(x: float) -> int:
    return 1-f(x)**2
