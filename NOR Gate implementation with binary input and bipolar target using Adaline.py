import numpy as np

# Define the NOR function inputs and corresponding bipolar outputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([1, -1, -1, -1])  # Bipolar target

# Initialize weights and bias
weights = np.zeros(inputs.shape[1])
bias = 0.0
learning_rate = 0.1
epochs = 100

# Adaline learning rule
for _ in range(epochs):
    for i in range(len(inputs)):
        linear_output = np.dot(inputs[i], weights) + bias
        error = outputs[i] - linear_output
        weights += learning_rate * error * inputs[i]
        bias += learning_rate * error

# Test the Adaline model
for i in range(len(inputs)):
    linear_output = np.dot(inputs[i], weights) + bias
    prediction = 1 if linear_output >= 0 else -1
    print(f"Input: {inputs[i]}, Prediction: {prediction}")