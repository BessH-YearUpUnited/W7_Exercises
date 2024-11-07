# Just a quick illustration that when running a loop over a 2-dimensional array, 
# the loop over the first dimension is returning the sub-arrays.

import numpy as np

arr = np.array([[1,1],[2,2]])

for i in arr:
    print(type(i))


# Looping over the next layer in our 2D array returns the elements, here integers

for i in arr:
    for x in i:
        print(type(x))