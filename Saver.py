from Network import Network


class State:
    def __init__(self, weights: list) -> None:
        self._weights = weights

    def get_weights(self) -> list:
        return self._weights


class Saver:
    def __init__(self, network: Network) -> None:
        self._states = []
        self._network = network

    def backup(self) -> None:
        self._states.append(self._network.save())

    def undo(self) -> None:
        if not len(self._states):
            return

        state = self._states.pop()
        try:
            self._network.restore(state)
        except Exception:
            self.undo()
