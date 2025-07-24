import numpy as np

array = np.arange(0,11)

# slicing can be used

# can change values of selected slice
array[:5] = 100
print(array)

# python does not create copies from slicing -> if a slice is stored in another variable and that slice is changed,
# the list that that slice is part of will also change
# must use array.copy() for a copy

# accessing elements in a bidimensional array
# array[index][index] or array[index,index]

# grad sub matrices
# use slicing -> array[:2,1:] everything to row 2 - not included, everything from column 1 to the end

# transform array to boolean variables
# bool_arr = arr > 5 -> each element will go through the condition and True or False will be appended based on the check

# THIS CAN BE USED TO MAKE CONDITIONAL SELECTION
# array[bool_array] => returns the array for the elements that are True
# it can be simplified to array[condition]