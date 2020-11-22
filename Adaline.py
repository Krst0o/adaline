import matplotlib.pyplot as plt
import numpy as np
import random


def fourier_transform(x):
    a = np.abs(np.fft.fft(x))
    a[0] = 0
    return a/np.max(a)


class Adaline(object):
    def __init__(self, no_of_input, learning_rate=0.01, iterations=100000):
        self.no_of_input = no_of_input
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.random.random(2*self.no_of_input + 1) - 0.5
        self.errors = []

    def _activation(self, x):
        return 1. / (1. + np.exp(-x))

    def _activation_derivative(self, x):
        return x * (1. - x)

    def train(self, training_data_x, training_data_y):
        for _ in range(self.iterations):
            e = 0

            random_input = random.choice(list(zip(training_data_x, training_data_y)))
            random_training_data = random_input[0].copy()
            random_training_label = random_input[1].copy()

            random_training_data = random_training_data * 0.8 + 0.1
            random_training_label = random_training_label * 0.8 + 0.1

            random_training_data = self._standarize(random_training_data)

            extended_training_data = np.concatenate([random_training_data, fourier_transform(random_training_data)])
            out = self.output(extended_training_data)

            self.weights[1:] += self.learning_rate * (random_training_label - out) * self._activation_derivative(out) * extended_training_data
            self.weights[0] += self.learning_rate * (random_training_label - out) * self._activation_derivative(out)
            e += 0.5 * (random_training_label - out) ** 2
            self.errors.append(e)
        plt.plot(range(len(self.errors)), self.errors)
        plt.savefig('errors.pdf')

    def _normalize(self, x):
        x_norm = np.copy(x)
        x_norm = (x_norm - np.min(x_norm)) / (np.max(x_norm) - np.min(x_norm))
        return x_norm

    def _standarize(self, x):
        x_norm = np.copy(x)
        x_norm = (x_norm - np.mean(x_norm)) / np.std(x_norm)
        return x_norm

    def output(self, input):
        summation = self._activation(np.dot(self.weights[1:], input) + self.weights[0])
        return summation

    def predict(self, input):
        input = self._standarize(input)
        input *= 0.8 + 0.1
        extended_input = np.concatenate([input, fourier_transform(input)])
        summation = self._activation(np.dot(self.weights[1:], extended_input) + self.weights[0])
        return summation
