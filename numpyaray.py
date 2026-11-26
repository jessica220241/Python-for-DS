
import numpy as np

marks = np.array(
    [72, 85, 49, 90, 67, 55, 38, 76, 81, 60, 45, 88]
)

# (a) Dimensions, shape and data type
print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Data type:", marks.dtype)

# (b) Mean, maximum, minimum and standard deviation
print("Mean:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Standard deviation:", marks.std())

# (c) Marks greater than or equal to 60
print("Marks >= 60:", marks[marks >= 60])

# (d) Count marks below 50
print("Marks below 50:", np.sum(marks < 50))

# (e) Reshape into 3 x 4 matrix
matrix = marks.reshape(3, 4)
print("3 x 4 Matrix:")
print(matrix)

# (f) Sum of each row
print("Sum of each row:", matrix.sum(axis=1))
