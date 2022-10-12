
import numpy as np

# numpy using arrays method
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# NumPy Arrays provides the ndim attribute
# that returns an integer that tells us how many dimensions

print(a.ndim)

# a is array of two dimensions

b = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [
             [9, 10, 11, 12], [13, 14, 15, 0]]])

# b is array of three dimensions
print(b.ndim)

# type in numpy is numpy.ndarray
print(type(b))

# NumPy arrays have an attribute called shape
# that returns a tuple with each index

print(b.shape)

# the attribute size is equal a length
# the diferent is iterator over the elements of the array
print(b.size)

arr = np.arange(20, 40, 4)

# the attribute 'arange' created a array
# utility the range for sentences
# example: (20, 40, 4): [20, 24, 28 ..... 40]

print(arr)

# because python include the native Solution
# example: list(range(10))

arr_filter = arr[(arr < 40) & (arr > 30)]

# filter the elements < 40 and >30
print(arr_filter)

arrayA = np.array([[2, 7], [0, 0]])
arrayB = np.array([[4, 2], [8, 1]])

# hstack
hsA = np.hstack((arrayA, arrayB))

print(hsA)
# the attribute 'hstack' created a array
# based in data sctructure stack


randoms = np.random.rand(100000)



