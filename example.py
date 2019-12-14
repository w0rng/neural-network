from network import Network
import activation_functions.sigmoid as sigmoid


def approximable(x: float) -> float:
    return 7*x**4 + 5*x**3 - 2*x**2 + x - 17


def main():
    network = Network([1, 3, 5, 3, 1], sigmoid.f, sigmoid.df)
    print(approximable(7), network.predict([7]))
    network.save("neurons.save")


if __name__ == "__main__":
    main()
