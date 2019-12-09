from math import log, exp


def f(x: float) -> float:
    return log(1+exp(x))


def df(x: float) -> float:
    return 1/(1+exp(-x))
