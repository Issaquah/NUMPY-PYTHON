import numpy as np

# create a random array of order 3x3
arr1 = np.random.rand(3, 3)
print("Array with random values=\n", arr1)

print("")

# calculate mean of created array
mean_of_array = arr1.mean()
print("Mean of created array=", mean_of_array)

print("")

# calculate mean of each row
mean_of_each_row = arr1.mean(axis=1)        # axis=1 to calculate mean of each row and return each mean as a 1-d array
print("Mean values of each rows=", mean_of_each_row)

print("")

# calculate mean of every column
mean_of_each_col = arr1.mean(axis=0)     # axis=0 to calculate mean of each column and return mean values as a 1-d array
print("Mean values of each column=", mean_of_each_col)

print("")

# calculate meadian of array
median = np.median(arr1, axis=0)
print(median)