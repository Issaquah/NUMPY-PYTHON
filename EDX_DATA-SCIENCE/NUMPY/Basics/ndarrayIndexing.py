import numpy as np

# create a matrix of order 3x4 and print
our_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [12, 13, 14, 15, 16]])
print(our_array)

print("")

# slice created array and form another different array
sliced_array = our_array[:2, 1:4]   # slice 1st and 2nd row and column 2nd,3rd,4th of row 1st and 2nd
print(sliced_array)

print("")

# modify sliced array
print("Sliced array before:\n", sliced_array)
sliced_array[0, 0] = 20
print("Sliced array after:\n", sliced_array)

print("")

# create a copy of our_array
copy_of_our_array = np.array(our_array[0:2, 0:2])
print(copy_of_our_array)

print("")

# slice the array and return it's dimensions
slices = our_array[0:1, :]
print(slices, slices.shape)