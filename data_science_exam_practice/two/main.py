#uses numpy
import numpy as np

#load the .npy matrix
image = np.loadtxt("2D_array.npy")

# binarize it, non-null bits = 1
binarized_image = np.where(image != 0, 1, 0)
print(binarized_image)

print("---------------------------------------------------------------------------------------")

# translate to right with 10 from the initial position
translated_matrix = np.roll(binarized_image, shift=110, axis=1)
print(translated_matrix)