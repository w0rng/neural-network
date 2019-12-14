import json
from neuron import Neuron


def save_neurons(matrix: list, filename: str) -> None:
    result = {}
    for num_layer, layer in enumerate(matrix):
        result[num_layer] = [neuron.weight for neuron in layer]
    file = open(filename, 'w')
    file.write(json.dumps(result))
    file.close()


def load_neurons(network, filename: str) -> None:
    file = open(filename, 'r')
    neurons = json.loads(file.read())
    file.close()
    matrix = []
    for num_layer in neurons:
        matrix.append([Neuron(layer) for layer in neurons[num_layer]])
    network.matrix = matrix
