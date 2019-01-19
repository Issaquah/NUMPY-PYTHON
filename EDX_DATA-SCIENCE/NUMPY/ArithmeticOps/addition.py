import numpy as np


our_array1 = np.array([[11, 22, 33], [12, 24, 36]], dtype=np.int32)     # create 2x2 array
our_array2 = np.array([[13, 26, 39], [14, 28, 42]], dtype=np.float32)
sum_of_arrays = np.add(our_array1, our_array2)                          # add both arrays like matrix element wise
print("Sum of both arrays = \n", sum_of_arrays)

print("")

product_of_arrays = np.multiply(our_array1, our_array2)
print("Product of both arrays = \n", product_of_arrays)