from network import Network
from activation_functions.sigmoid import f, df


def approximable(x: float) -> float:
    return 7*x**4 + 5*x**3 - 2*x**2 + x - 17


def main():
    network = Network([1, 3, 5, 3, 1], f, df)
    print(approximable(7), network.predict([7]))


if __name__ == "__main__":
    main()
