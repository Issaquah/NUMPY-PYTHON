import numpy as np

# create simple array of only 0s
array_of_zeroes = np.zeros((3, 3))
print(array_of_zeroes)

print("")

# create array of 1s
array_of_ones = np.ones((3, 3))
print(array_of_ones)

print("")

# create a matrix with 1 diagonal on 1s and other as 0s
diagonal_matrix = np.eye(3, 3)
print(diagonal_matrix)

print("")

# create a matrix with random values
matrix_with_random_values = np.random.random((3, 3))
print(matrix_with_random_values)

print("")
# create a matrix filled with a specific value
dedicated_matrix = np.full((2, 3), 4)
print(dedicated_matrix)