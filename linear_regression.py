import numpy as np


class LinearRegression:

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.rate=learning_rate
        self.iterations=n_iters
        self.w=None
        self.w0=None

    def fit(self, X, y):
        m, num=X.shape
        self.w=np.zeros(num)
        self.w0=0

        for _ in range(self.iterations):
            hipothesis=np.dot(X, self.w) + self.w0
            self.w-=self.rate * (1 / m) * np.dot(X.T, (hipothesis - y))
            self.w0-=self.rate * (1 / m) * np.sum(hipothesis - y)

    def predict(self, X):
        predicted=np.dot(X, self.w) + self.w0
        return predicted