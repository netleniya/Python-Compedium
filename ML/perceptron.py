import numpy as np


class Perceptron:
    def __init__(self, eta=0.01, epochs=50, random_state=1) -> None:
        self.eta: float = eta
        self.epochs: int = epochs
        self.random_state: int = random_state
