import numpy as np

inputs = [
    [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0],
    [0.2, 0.4, 0.6, 0.8, 1.0, 0.1, 0.3, 0.5, 0.7, 0.9],
    [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 0.1],
    [1.2, 1.4, 1.6, 1.8, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1],
    [0.0, 0.8, 0.1, 5.5, 0.5, 0.3, 8.0, 0.6, 0.9, 1.5],
]
weights = [
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 0.0],
    [1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],
    [1.2, 9.4, 6.1, 2.4, 9.6, 3.1, 2.7, 5.4, 7.3, 4.3],
    [4.4, 6.2, 3.2, 4.7, 4.8, 3.5, 3.8, 8.4, 3.4, 2.1],
    [7.3, 3.5, 2.7, 3.8, 5.3, 3.8, 5.4, 3.2, 7.3, 3.8],
]
biases = [2.5, 8.4, 5.7, 2.6, 4.2]
weights2 = [
    [2.6, 2.8, 4.3, 2.9, 9.6],
    [5.3, 2.8, 4.8, 6.5, 3.7],
    [1.8, 4.2, 0.8, 4.9, 4.3],
]

biases2 = [2.7, 3.0, 7.5]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
print(layer2_outputs)
