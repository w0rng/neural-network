from types import FunctionType
from neuron import Neuron
import saver


class Network:
    def __init__(self, count_neurons: list,
                 f: FunctionType,
                 df: FunctionType) -> None:
        self.f = f
        self.df = df
        self.matrix = []
        if len(count_neurons) >= 2:
            self.__create_matrix(count_neurons)
        else:
            exit(2)

    def __create_matrix(self, count_neurons: list) -> None:
        for count in count_neurons:
            self.matrix.append([Neuron() for _ in range(count)])
        self.__gen_weights(count_neurons)

    def __gen_weights(self, count_neurons: list) -> None:
        for i, layer in enumerate(self.matrix):
            for neuron in layer:
                if i != len(self.matrix) - 1:
                    neuron.gen_weight(count_neurons[i + 1])
                else:
                    neuron.weight = [1]

    def predict(self, data: list) -> list:
        normalization_factor = max(data)
        data = [x/normalization_factor for x in data]
        for i, layer in enumerate(self.matrix):
            for j, neuron in enumerate(layer):
                if i == 0:
                    neuron.inp = data[j]
                else:
                    inp = [n.inp * n.weight[j] for n in self.matrix[i - 1]]
                    neuron.inp = self.f(sum(inp))
        return [self.f(n.inp) * normalization_factor for n in self.matrix[-1]]

    def save(self, filename: str) -> None:
        saver.save_neurons(self.matrix, filename)
