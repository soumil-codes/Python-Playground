import numpy as np

a = np.array([15,2,33,4,5]).reshape((1,5))
print(a)
b = np.dot(a.T, a)
print(b)

b= np.linalg.inv(b)

# c= np.dot(a, b)

# print(c)

