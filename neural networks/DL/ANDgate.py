import numpy as np

x = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0,0,0,1])

def activation(x):
    return 1 if x >= 0 else 0

weights = np.zeros(x.shape[1])
bias = 0


epochs = 1000
n = 0.01
for _ in range(epochs):
    for i in range(len(x)):
        z = np.dot(x[i], weights) + bias
        ypred = activation(z)
        error = y[i] - ypred

        weights += error*n*x[i]
        bias += error*n


print(weights)
print(bias)


x = np.array([1,0])
k = np.dot(x, weights) + bias
output = activation(k)
print(output)