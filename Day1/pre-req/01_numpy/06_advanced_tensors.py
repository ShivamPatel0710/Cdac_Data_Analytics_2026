import numpy as np

A = np.array([[1, 2], [3, 4]])
print("Matrix A:\n", A)
B = np.array([[5, 6], [7, 8]])
print("Matrix B:\n", B)
mat_mul = np.einsum('ij,jk->ik', A, B)  # Matrix multiplication using Einstein summation
print("Matrix Multiplication (A * B):\n", mat_mul)

print("_" * 50)
print("_" * 50)

transpose_einsum = np.einsum('ij->ji', A)  # Transpose using Einstein summation
print("Transpose of Matrix A:\n", transpose_einsum)

trace_einsum = np.einsum('ii->', A)  # Trace(sum of diagonal elements) using Einstein summation
print("Trace of Matrix A:", trace_einsum)
print("Validating Trace Calculation:", np.trace(A))  # Validating with numpy's built-in trace function

print("="*60)

# nd Array to simulate pytorch tensor operations(Batch, Channels, Height, Width)
tensor_A = np.zeros((2, 3, 4, 4))  # Simulating a batch of 2 images with 3 channels and 4x4 dimensions
print("Tensor A Shape:", tensor_A.shape)
print("Tensor A:\n", tensor_A)

# convert axes from pytorch(NCHW) to tensorflow(NHWC) format using einsum
tf_tensor = np.einsum('nchw->nhwc', tensor_A)  # Reordering axes using Einstein summation
tf_tensor_np = np.transpose(tensor_A,(0,2,3,1)) # using transpose for comparison
print("tf_tensor Shape:", tf_tensor.shape)
print("tf_tensor_np Shape:", tf_tensor_np.shape)
# print("Tensor A in TensorFlow Format (NHWC):\n", tf_tensor)
print("="*60)