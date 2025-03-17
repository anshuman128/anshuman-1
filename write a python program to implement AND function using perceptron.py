import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.W = np.zeros(input_size + 1)  # +1 for the bias term
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = self.W.T.dot(np.insert(x, 0, 1))  # Insert bias term
        return self.activation_function(z)

    def fit(self, X, d):
        for epoch in range(self.epochs):
            for i in range(d.shape[0]):
                x_i = np.insert(X[i], 0, 1)  # Insert bias term
                y_i = self.predict(X[i])
                error = d[i] - y_i
                self.W = self.W + self.learning_rate * error * x_i

# AND logic function
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

d = np.array([0, 0, 0, 1])  # Desired output for AND

# Creating perceptron
perceptron = Perceptron(input_size=2)
perceptron.fit(X, d)

# Testing perceptron
print("Testing AND Perceptron")
for x in X:
    print(f"Input: {x}, Output: {perceptron.predict(x)}")
