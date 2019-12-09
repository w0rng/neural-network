from random import uniform as rand


class Neuron:
    def __init__(self, weight: list = None, inp: int = 0) -> None:
        self.weight = weight if weight else []
        self.inp = inp

    def gen_weight(self, count: int) -> None:
        self.weight = [rand(-0.5, 0.5) for _ in range(count)]
