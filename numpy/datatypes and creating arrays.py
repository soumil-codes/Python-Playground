import numpy as np

# ---------------------- lecture 1 ------------------------
# what is numpy


# numPy is a python library that helps with scientific computing
# it provides multidimentional arrays, various derieved objects


# x = np.array([1,2,3,4]) #array
# y = [1,2,3,4]           #list

# print(x)
# print(type(x))
# print(y)



# -------------------- lecture 2 ---------------------------
# difference between numpy array and python list


# a = [j**4 for j in range(1,9000000)]   #1.01 sec
# a = np.arange(1,9000000)**4            #0.20 sec (faster)

# ----------------------- lecture 3 ----------------------------
# dimention of array


# ar1 = np.array([1,2,3,4])
# ar2 = np.array([[1,2,3,4],[5,6,7,8]])
# ar3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

# print(ar1)
# print(ar2)
# print(ar3)

# print(ar1.ndim, ar2.ndim, ar3.ndim)


# -------------------------- lecture 4 ---------------------------------
# how to create numpy array

# ZEROES

# ar_zero = np.zeros(4)
# print(ar_zero)
# print()
# ar_zerond = np.zeros((2,3,4,5,6))
# print(ar_zerond)

# ONES

# ar_one = np.ones(4)
# print(ar_one)
# print()
# ar_onend = np.ones((2,3,4,5,6))
# print(ar_onend)

# EMPTY

# ar_emt = np.empty(4)
# print(ar_emt)

#RANGE

# ar_rn = np.arange(7,)
# print(ar_rn)
