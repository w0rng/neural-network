from math import sin, cos


def f(x: float) -> float:
    if x == 0:
        return 1
    else:
        return sin(x)/x


def df(x: float) -> float:
    if x == 0:
        return 0
    else:
        return cos(x)/x - sin(x)/(x**2)
