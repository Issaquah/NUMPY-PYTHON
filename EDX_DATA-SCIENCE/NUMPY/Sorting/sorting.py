import numpy as np

random_array = np.random.rand(10)               # generate array of random values
unsorted_array = np.array(random_array)
print("Unsorted array=\n", unsorted_array)
print("")
sorted_array = np.sort(unsorted_array)          # use sort to arrange array elements in ascending order
print("Sorted array=\n", sorted_array)
print("")
unsorted_array.sort()                           # call sort() on unsorted array to do as stated in above comment
print("Sorted array by calling sort() on unsorted_array=\n", unsorted_array)


print("")

# pull out only unique values from arrays
first_array = np.array([1, 11, 3, 4, 5, 2, 11, 19, 5, 1, 2, 13, 7, 19])
print("Unique elements from 1st array=", np.unique(first_array))

print("")

# find out unique elements from 1st and 2nd array
# use intersectId() and pass 1st and 2nd array to find unique values
second_array = np.array([1, 11, 23, 14, 5, 12, 11, 9, 5, 19, 22, 13, 3, 7, 19])
print("Unique elements from 1st and 2nd array=", np.intersect1d(first_array, second_array))

print("")

# you can clearly understand what's executing below this comment. Hail NumPy!!!
print("Sum of all elements of 1st array=", first_array.sum())
print("")
b = 1
print(first_array + b)
