import numpy as np

x = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1],
])

y = np.array([0,1,1,0])

w1 = np.array([[1, -1],
               [-1, 1]])   
b1 = np.array([[0, 0]])

w2 = np.zeros((2,1))
b2 = np.zeros((1,1))

def activation(x):
    return np.where(x >= 0, 1, 0)

n = 0.01
epochs = 1000

for _ in range(epochs):
    for i in range(len(x)):
        z1 = np.dot(x[i], w1) + b1
        a1 = activation(z1)
        z2 = np.dot(a1, w2) + b2
        a2 = activation(z2)

        error = y[i] - a2

        w2 += n* a1.reshape(-1,1) * error
        b2 += n* error


for i in range(len(x)):
    z1 = np.dot(x[i], w1) + b1
    a1 = activation(z1)
    z2 = np.dot(a1, w2) + b2
    a2 = activation(z2)
    print(f"{x[i]} -> {a2[0]}")


# import numpy as np

# y = np.array([0,1,1,0])
# x = np.array([
#     [0,0],
#     [0,1],
#     [1,0],
#     [1,1]
# ])

# w1 = np.array([
#     [-1,-1],
#     [-1,1],
#     [1,-1],
#     [1,1]
# ])

# b1 = np.array([
#     [-1],
#     [-1],
#     [-1],
#     [-1]
# ])

# w2 = np.random.randn((4,1))
# b2 = np.random.randn((1,1))

# def activation(x):
#     return 

