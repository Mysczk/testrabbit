import numpy as np

class Calculator:
    def add(a, b):
        return np.add(a, b)

    def subtract(a, b):
        return np.subtract(a, b)

    def multiply(a, b):
        return np.multiply(a, b)

    def divide(a, b):
        if np.any(b == 0):
            raise ValueError("Cannot divide by zero")
        return np.divide(a, b)