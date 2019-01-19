import numpy as np

our_array = np.array([[21, 22, 23, 24], [25, 28, 27, 29], [31, 30, 26, 20], [34, 38, 40, 32]], dtype= np.int32)
print(our_array)

print("")

# filter array based on condition
filter = (our_array > 24)           # check each index if > 24 and return true or false
print(filter)

print("")

# print filtered array elements which are true according to condition below
print(our_array[filter])

# print filtered array elements which are true according to condition below
print(our_array[our_array > 28])

print("")

# print filtered array elements which are true according to condition below
print(our_array[(our_array % 2 == 0) & (our_array > 30)])

print("")

# print filtered array elements which are true according to condition below
our_array[(our_array % 2 == 0) & (our_array > 30)] += 100
print(our_array)