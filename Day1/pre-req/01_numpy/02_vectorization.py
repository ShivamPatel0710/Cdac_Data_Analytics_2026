import numpy as np

inch_measurements = np.array([1.0, 2.5, 5.0, 10.0])
centimeter_measurements = inch_measurements * 2.54 # vecorized operation to convert inches to centimeters
print("Inch Measurements:", inch_measurements)
print("Centimeter Measurements:", centimeter_measurements)

feature_a = np.array([1, 2, 3, 4])
feature_b = np.array([10, 20, 30, 40])

print("Feature A:", feature_a)
print("Feature B:", feature_b)
print("Sum of Features:", feature_a + feature_b) # vectorized addition
print("Difference of Features:", feature_a - feature_b) # vectorized subtraction
print("Product of Features:", feature_a * feature_b) # vectorized multiplication
print("Quotient of Features:", feature_a / feature_b) # vectorized division

# Algorithmic rigor
rng = np.random.default_rng(seed=42)  # Create a random number generator with a fixed seed for reproducibility
signal_data = rng.uniform(low=0.0, high=1.0, size=(4,4))  
print("Signal Data:\n", signal_data)

# vectorized masking operation to filter out values below 0.5
mask = signal_data > 0.7
print("Mask:\n", mask)
filtered_signal_data = signal_data[mask]
print("Filtered Signal Data:\n", filtered_signal_data)
print("_" * 40)
# data type rigor
int_implicit = np.array([1, 2, 3, 4])  # default data type is int64
int_explicit = np.array([1, 2, 3, 4], dtype=np.int32)  # explicitly set data type to int32
print("Implicit Integer Array:", int_implicit, "Data Type:", int_implicit.dtype)
print("Explicit Integer Array:", int_explicit, "Data Type:", int_explicit.dtype)
print("_" * 40)

# size of items
print("Size of Implicit Integer Array:", int_implicit.itemsize, "bytes")
print("Size of Explicit Integer Array:", int_explicit.itemsize, "bytes")

print("_" * 40)
# numpy character code for dtypes
print("Numpy Character Code for DTypes")
print("int32:", np.dtype(np.int32).char)
print("int64:", np.dtype(np.int64).char)    
print("float32:", np.dtype(np.float32).char)
print("float64:", np.dtype(np.float64).char)

 # getting dtypes from character codes
print("DType from Character Code 'i':", np.dtype('i')) # integer
print("DType from Character Code 'f':", np.dtype('f')) # single precision float
print("DType from Character Code 'd':", np.dtype('d')) # double precision float
print("DType from Character Code 'i4':", np.dtype('i4')) # 32-bit integer
print("DType from Character Code 'U10':", np.dtype('U10')) # u10 means unicode string of length 10
print("DType from Character Code 'f2':", np.dtype('f2')) # 16-bit float

print("_" * 60)

# custom structured data type
structured_dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
print("Structured DType:", structured_dtype)
print("_" * 40)
employee_data = np.array([('Alice', 30, 5.5), ('Bob', 25, 6.0), ('Charlie', 35, 5.8)], dtype=structured_dtype)
print("Employee Data:\n", employee_data)
telemetric_schema = np.dtype([('device_id', str, 16),('status_code',np.int32)])
print("Telemetric Schema DType:", telemetric_schema)

