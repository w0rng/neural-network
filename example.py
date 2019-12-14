from network import Network
import activation_functions.sigmoid as sigmoid


def approximable(x: float) -> float:
    return 7*x**4 + 5*x**3 - 2*x**2 + x - 17


def main():
    network = Network([1, 10, 20, 30, 20, 10, 1], sigmoid.f, sigmoid.df)
    network.save("neurons.save")
    print(approximable(7), network.predict([7]))


if __name__ == "__main__":
    main()
