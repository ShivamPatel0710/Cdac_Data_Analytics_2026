'''
numpy slicing is a powerful feature that allows you to extract specific portions of an array. It enables you to access elements, rows, columns, or subarrays using a concise and efficient syntax. Slicing can be done using the colon (:) operator, which specifies the start and end indices of the slice.

 Advantages of numpy slicing include:
 1. Zer0-copy views: sharing underlying buffer with original array, which saves memory and improves performance.
 2. Flexible indexing: allows for easy extraction of specific elements, rows, or columns.
 3. Boolean indexing: Allows you to selsect elements based on conditions, enabling powerful filtering capabilities.
'''

import numpy as np
sensor_reading = np.arange(9)
print("Original Array:", sensor_reading)
sensor_reading[2] = 99
print("Modified Array:", sensor_reading)
print("Sliced Array (2:5):", sensor_reading[2:5])  # Slicing from index 2 to 4

# tensor change
sensor_reading[2:5] = 1000  # Modifying the sliced portion
print("Modified Array after Slicing:", sensor_reading) # values at 2 to 4 are changed to 1000

print("_" * 50)
values = np.arange(10,101,10)
print("Original Values:", values)
print("values[2]", values[2])  # Accessing the element at index 2
print("values[2:]", values[2:])  # Slicing from 2 to end
print("values[2:5]", values[2:5])  # Slicing from index 2 to 4
print("values[:5]", values[:5])  # Slicing from start to index 4
print("values[1:8:2]", values[1:8:2])  # Slicing from index 1 to 7 with a step of 2
print("values[-1]", values[-1])  # Accessing the last element
print("values[-3:]", values[-3:])  # Slicing from third-to-last till the end
print("values[:-3]", values[:-3])  # Slicing from start to third-to-last
print("values[-5:-2]", values[-5:-2])  # Slicing from fifth-to-last to third-to-last
print("values[-2:-5]", values[-2:-5])  # Slicing from second-to-last to fifth-to-last (empty slice)
print("values[-5:-2:-1]", values[-5:-2:-1])  # Slicing from fifth-to-last to third-to-last in reverse order
print("values[-2:-5:-1]",values[-2:-5:-1])  # Slicing from second-to-last to fifth-to-last in reverse order
print("values[::-1]", values[::-1])  # Reversing the array
print("_" * 50)

feature_matrix = np.array([[1, 2, 3,4], [ 5, 6, 7, 8], [ 9, 10, 11, 12], [ 13, 14, 15, 16]])
print("Feature Matrix:\n", feature_matrix)
print("feature_matrix[1]:", feature_matrix[1])  # Accessing the element at row 1, column 2
print("feature_matrix[1, 2]:", feature_matrix[1, 2])  # Accessing the element at row 1, column 2
print("feature_matrix[:2]:", feature_matrix[:2])  # Accessing the first two rows
print("feature_matrix[:, 2]:", feature_matrix[:, 2])  # Accessing the third column
print("feature_matrix[1:3]:", feature_matrix[1:3])  # Accessing rows 1 and 2
print("_" * 50)

matrix= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
row_rank1 = matrix[1, :]  # 1 d array
print("Row Rank 1:", row_rank1) 
row_rank2 = matrix[1:2, :]  # 2d array
print("Row Rank 2:\n", row_rank2)
#string interpolation to print the shape of the arrays
print(f"Shape of Row Rank 1: {row_rank1.shape}")  # Output: (3,)
print(f"Shape of Row Rank 2: {row_rank2.shape}")  # Output: (1, 3)

# column extraction
col_rank1 = matrix[:, 0]  # 1 d array
print("Column Rank 1:", col_rank1)
col_rank2 = matrix[:, 0:1]  # 2d array
print("Column Rank 2:\n", col_rank2)
print("_" * 50)
print("_" * 50)

print("Original Matrix:\n", matrix)
row_indices = np.arange(4)  # Array of indices [0, 1, 2, 3]
col_incices = np.array([0,2,0,1]) # Column indicies as target
extracted_elements = matrix[row_indices, col_incices]  # Extracting elements using advanced indexing
print("Extracted Elements:", extracted_elements)  # Output: [1, 6, 7, 11]
print("_" * 50)
print("_" * 50)

