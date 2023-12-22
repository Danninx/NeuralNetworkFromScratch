# Single Neuron
inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = sum([inputs[i]*weights[i] for i in range(len(inputs))]) + bias
print(output)