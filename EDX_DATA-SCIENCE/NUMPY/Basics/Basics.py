import numpy as np

# create and print an array
our_array = np.array([1, 2, 3, 4, 5])
print(our_array)

print("")

# print dimension of the array
dimensions_of_array = our_array.shape
print(dimensions_of_array)

print("")

# access elements of array
print(our_array[0])
print(our_array[2])
print(our_array[4])

print("")

# modify array
our_array[1] = 666
print(our_array)

print("")

# create 2-d array
next_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(next_array)

print("")

# print shape of array
shape_of_array = next_array.shape
print(shape_of_array)

print("")

# access elements from 2-d array
first_number = next_array[0, 1]    # 2nd element of 1st row
second_number = next_array[1, 4]   # 5th element of 2nd row
third_number = next_array[1, 3]   # 4th element of 2nd row
fourth_number = next_array[0, 0]   # 1st element of 1st row
fifth_number = next_array[1, 0]   # 1st element of 2nd row

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)
print(fifth_number)