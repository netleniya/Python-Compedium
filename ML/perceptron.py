import numpy as np


class Perceptron:
    """
    Implements a simple Perceptron classifier.

    The Perceptron is a type of linear classifier, which means it classifies data by finding the best hyperplane that separates the two classes. It learns the weights of the input features by iteratively adjusting them based on the classification errors.

    Parameters:
        eta (float): The learning rate (between 0.0 and 1.0).
        epochs (int): The number of passes through the training dataset.
        random_state (int): The seed used by the random number generator.

    Attributes:
        w_ (ndarray): The weights after fitting.
        errors_ (list): The number of misclassifications in every epoch.
    """

    def __init__(self, eta=0.01, epochs=50, random_state=1) -> None:
        self.eta: float = eta
        self.epochs: int = epochs
        self.random_state: int = random_state

    def fit(self, X, y):
        """
        Fits the Perceptron model to the provided training data.

        Parameters:
            X (ndarray): The training input samples.
            y (ndarray): The target (class) values.

        Returns:
            self (Perceptron): The fitted Perceptron instance.
        """
        rgen = np.random.default_rng(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.epochs):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """
        Calculates the net input of the Perceptron model by taking the dot product of the input samples `X` and the weights `self.w_[1:]`, and adding the bias term `self.w_[0]`.

        Parameters:
            X (ndarray): The input samples.

        Returns:
            float: The net input of the Perceptron model.
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """
        Predicts the class labels for the input samples `X`.

        Parameters:
            X (ndarray): The input samples.

        Returns:
            ndarray: The predicted class labels.
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)
