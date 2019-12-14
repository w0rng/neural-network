import json


def save_neurons(matrix: list, filename: str) -> None:
    result = {}
    for num_layer, layer in enumerate(matrix):
        result[num_layer] = [neuron.weight for neuron in layer]
    file = open(filename, 'w')
    file.write(json.dumps(result))
    file.close()
