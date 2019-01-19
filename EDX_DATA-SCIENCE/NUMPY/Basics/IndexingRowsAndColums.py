import numpy as np

# create an array of order 4x4
our_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Initial array\n", our_array)

print("")

# create array of specific row and column indexes
# array holds indexes of elements present at the positions specified in the array\
# so this allows accessing elements by specifying it's position in the array
row_index = np.array([0, 1, 2, 3])              # array of indexes of each row
col_index = np.array([0, 1, 2, 3])              # array of indexes of each column
for i in zip(row_index, col_index):             # using zip function to iterate through the arrays created
    print(i)

print("")

# access values from array by accessing row and column index
# by specifying row and col index in array we can specify the elements present at that particular index
print("Array after using row indexing:", our_array[row_index, col_index])

print("")

# modify array by modifying specific elements in array of row and col index
print("Array before modifying elements at the indices specified in row and col index\n", our_array)
our_array[row_index, col_index] += 100
print("Array after modifying elements at the indices specified in row and col index\n", our_array)