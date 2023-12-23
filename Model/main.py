# Single Neuron
inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
bias = [
    2,
    3,
    0.5
]

output = []

for i in range(len(weights)):
    w = weights[i]
    b = bias[i]
    output.append(sum([inputs[j]*w[j] for j in range(len(inputs))]) + b)

print(output)