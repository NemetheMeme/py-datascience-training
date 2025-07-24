import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data =[10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

my_series = pd.Series(data = my_data, index= labels)

series_from_dictionary = pd.Series(d)
series_from_numpy_array = pd.Series(arr)

# iterate over a series of functions and call them upon a
def add_5(x): return x + 5
def square(x): return x * x
def half(x): return x / 2

# Store them in a Series
funcs = pd.Series([add_5, square, half])
value = 2

value = funcs[0](value)
print(value)