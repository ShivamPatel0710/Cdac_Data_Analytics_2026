import numpy as np
x = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float64)
y = np.array([[5.0, 6.0], [7.0, 8.0]], dtype=np.float64)

print("x + y =\n", np.add(x, y))  # Element-wise addition function used = np.add(x, y)
print("x - y =\n", np.subtract(x, y))  # Element-wise subtraction function used = np.subtract(x, y)
print("x * y =\n", np.multiply(x, y))  # Element-wise multiplication function used = np.multiply(x, y)
print("x / y =\n", np.divide(x, y))  # Element-wise division function used = np.divide(x, y)
print("sqrt(x) =\n", np.sqrt(x))  # Element-wise square root function used = np.sqrt(x)

print("_" * 50)
print("_" * 50)

raw_signals = np.array([-1.7,-0.2,0.5,1.4,2.8])
print("Raw Signals:", raw_signals)
print("Floor of Raw Signals:", np.floor(raw_signals))  # Element-wise floor function used = np.floor(raw_signals) look for next whole number
print("Ceil of Raw Signals:", np.ceil(raw_signals))  # Element-wise ceil function used = np.ceil(raw_signals) look for previous whole number
print("Round of Raw Signals:", np.round(raw_signals))  # Element-wise round function used = np.round(raw_signals)

print("_" * 50)
print("_" * 50)

dataset = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Dataset:\n", dataset)

# Global Reduction Operations
print("Sum of all elements:", np.sum(dataset))  # Sum of all elements in the dataset
print("Mean of all elements:", np.mean(dataset))  # Mean of all elements in the dataset
print("_" * 50)

# axis=0 Operations (Column-wise)
print("Sum of each column:", np.sum(dataset, axis=0))  # Sum of each column
print("Mean of each column:", np.mean(dataset, axis=0))  # Mean of each column
print("_" * 50)

# axis=1 Operations (Row-wise)
print("Sum of each row:", np.sum(dataset, axis=1))  # Sum of each row   
print("Mean of each row:", np.mean(dataset, axis=1))  # Mean of each row
print("_" * 50)

raw_features=np.array([
    [150.0, 2.5, 12.0],
    [170.0, 3.8, 15.0],
    [140.0,1.9, 10.0],
    [180.0,4.2,18.0]
])

col_means = np.mean(raw_features, axis=0)  # Mean of each column
col_stds = np.std(raw_features, axis=0)  # Standard deviation of each column

'''
formula for standard deviation = sqrt(sum((x - mean)^2) / n)
step 1: calculate the mean of each column
step 2: subtract the mean from each element in the column
step 3: square the result of step 2
step 4: sum the squared results of step 3
step 5: divide the sum from step 4 by the number of elements in the column
'''

print("Column Means:", col_means)
print("Column Standard Deviations:", col_stds)

# compute standardized features using broadcasting z-score normalization
standardized_features = (raw_features - col_means) / col_stds
print("Standardized Features:\n", standardized_features)