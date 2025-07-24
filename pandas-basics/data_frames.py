import numpy as np
import pandas as pd
from numpy.random import randn

def print_new_line():
    print('--------------------------------------')

np.random.seed(101)

#DataFrame(data,rows,columns)
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print_new_line()

# select a column
W_column_data = df['W']  # equivalent of df.W  / df.ColumnName
# print(W_column_data)
# print(W_column_data.sum())
print(df.W)
print_new_line()

# select multiple columns
WZ = df[['W', 'Z']]
print(WZ)
print_new_line()

# select  rows
print(df.loc[['A', 'D']])
print_new_line()

# get the row based on index not key
print(df.iloc[[0,3]])
print_new_line()

# add new columns
df['new'] = 0
print(df)
print_new_line()

# to drop a column
# axis 0  = x axis, axis 1 = y axis
# must reassign, or use the inplace
#df = df.drop('new', axis = 1)
df.drop('new', axis = 1, inplace = True)
print(df)
print_new_line()

print('shape:', df.shape)
print_new_line()

# conditional selection using bracket notation
# df > 0  => returns True or False
booldf = df >  0
print(df[booldf])
# or just use the condition into the brackets df[df > 0]
print_new_line()

# can do the same thing for  specified columns or rows
print(df.loc['B'] > 0)
# print(df.iloc[1,2] > 0)

