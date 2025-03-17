import numpy as np

# Define p.array([-1, 1, 1, -1])  # Bipolar target

# Initialize weights and bias for each Adaline unit
weights1 = np.random.rand(2)
weights2 = np.random.rand(2)
bias1 = np.random.rand()
bias2 = np.random.rand()
learning_rate = 0.1
epochs = 100

# Madaline learning rule
for _ in range(epochs):
    for i in range(len(inputs)):
        linear_output1 = np.dot(inputs[i], weights1) + bias1
        linear_output2 = np.dot(inputs[i], weights2) + bias2
        output1 = 1 if linear_output1 > 0 else -1
        output2 = 1 if linear_output2 > 0 else -1

        combined_output = 1 if output1 != output2 else -1
        error = outputs[i] - combined_output

        # Update the weights and bias for both Adalines
        if error != 0:
            weights1 += learning_rate * error * inputs[i]
            bias1 += learning_rate * error
            weights2 += learning_rate * error * inputs[i]
            bias2 += learning_rate * error

# Test the Madaline model
for i in range(len(inputs)):
    linear_output1 = np.dot(inputs[i], weights1) + bias1
    linear_output2 = np.dot(inputs[i], weights2) + bias2
    output1 = 1 if linear_output1 > 0 else -1
    output2 = 1 if linear_output2 > 0 else -1

    combined_output = 1 if output1 != output2 else -1
    print(f"Input: {inputs[i]}, Prediction: {combined_output}")
the XOR function inputs and corresponding bipolar outputs
inputs = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
outputs = n