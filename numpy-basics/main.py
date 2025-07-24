#pip install numpy
import numpy as np
import numpy as numpy

# create arrays
py_list = [1,2,3]
array = np.array(py_list)
double_dimension_array = np.array([[1,2,3],[4,5,6]])
print('Numpy array: {}, {}'.format(type(array),array))

# create aray in a range and with a step np.arange(start,stop,step)
np.arange(0,10)

#create an array initialized as 0
zeros = np.zeros(4)
tuple_zeros = np.zeros((5,5))

# np.linspace(start, stop, num), where num is specifying: i want num numbers evenly splitted between the boundary of [start,stop]
# similar to np.arange
linspace_array = np.linspace(0,2,5)
print('lispace array - ', linspace_array)

# creates an array/multi-dimensional array of ones
np.ones((3,4))

# creates an Identity matrix - multi-dimensional array
np.eye(3)

# create random arrays
np.random.rand(4)
# double dimensional
np.random.rand(5,5)

# get random samples from the standard normal distribution / Gaussian distribution
np.random.randn(3)

# np.random.randint(start, stop, num_count) - get random integer between boundary
# stop bound not included
np.random.randint(1,100)

# reshape the array
# important - check if columns*row == array's length
# arr.reshape(5,5)

# max and min values of the arrays => .max() or .min()
# return the index location of the max or min - .argmax(), .argmin()
# return the shape of the array : arr.shape -> return for example (25,) -> unidimensional array of 25 values
# get datatype of the array : array.dtype