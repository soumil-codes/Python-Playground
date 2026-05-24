# we have taken a neuron connencted to 3 previous neurons (weights) which act as a input for it now
# the values taken are random

inputs = [1.2, 5.5, 3.3]
weights = [3.9, 8.5, 1.1]
bias = 3 # bias is unipue to a neuron 

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

print(output)