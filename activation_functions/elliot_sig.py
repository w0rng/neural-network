def f(x: float) -> float:
    return x/(1+abs(x))


def df(x: float) -> float:
    return 1/(1+abs(x))**2
