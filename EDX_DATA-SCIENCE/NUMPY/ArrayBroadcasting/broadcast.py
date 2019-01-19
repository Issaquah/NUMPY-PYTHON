import numpy as np

first_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [2, 4, 6, 8]])
second_array = np.array([0, 2, 3, 7])

final_array = first_array + second_array
print("Broadcasting 1st with 2nd array=\n", final_array)

print("")

third_array = np.eye(3, 3)
print("Just an array of diagonals as 1s=\n", third_array)

print("")

second_array = second_array[np.newaxis]
new_array = first_array + second_array
print("Transpose of 2nd array=", second_array)
print("")
print("Broadcasting 1st with 2nd array after transposing 2nd array=\n", new_array)
