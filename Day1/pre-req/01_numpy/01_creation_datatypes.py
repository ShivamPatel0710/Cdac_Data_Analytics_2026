'''
Numpy :
Memory Model :
Type Precision :
Structured Schemas :
'''
# create a virtual environment
# use "python -m venv <env_name>" to create a virtual environment
# activate the virtual environment : ~/.DA/Scripts/activate.psl 
# pip install numpy

import numpy as np
import sys

print("Python Version:", sys.version)
print("NumPy Version:", np.__version__)
print("Python Version Info:", python_version := sys.version_info)

vector_1d = np.array([1, 2, 3, 4, 5])
matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("1D Vector:", vector_1d)
print("2D Matrix:\n", matrix_2d)
print("-"*60)

#memory footprint comparison
size = 10000
python_list = list(range(size))
numpy_array = np.arange(size)
actual_size = sys.getsizeof(python_list) + sum(sys.getsizeof(item) for item in python_list)
print("Memory size of Python list:", actual_size, "bytes")

print("Memory size of NumPy array:", numpy_array.nbytes, "bytes")
print("-"*60)

#list comprehension vs generator expression
# val = 10000
# list_comp = [val for val in range(val)]
# print("List Comprehension Memory Size:", sys.getsizeof(list_comp), "bytes")

# gen_expr = (val for val in range(val))
# print("Generator Expression Memory Size:", sys.getsizeof(gen_expr), "bytes")
# print("")
# print("-"*60)


# numpy tensor initialization
#tensor factory methods
zero_matrix = np.zeros((3, 4))
one_matrix = np.ones((2, 3))
constant_matrix = np.full((2, 3), 7)
ident_matrix = np.eye(3)

random_rng = np.random.default_rng(seed=42)
random_matrix = random_rng.random((3, 3))

print("Zero Matrix:\n", zero_matrix)
print("One Matrix:\n", one_matrix)
print("Constant Matrix:\n", constant_matrix)
print("Identity Matrix:\n", ident_matrix)
print("Random Matrix:\n", random_matrix)