import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 矩阵加法
C = np.add(A, B)
print("A + B: \n", C)

# 矩阵减法
D = np.subtract(A, B)
print("A - B: \n", D)

# 矩阵乘法
E = np.dot(A, B)
print("A * B: \n", E)

# 矩阵转置
F = np.transpose(A)
print("A的转置: \n", F)

# 矩阵的逆
G = np.linalg.inv(A)
print("A的逆: \n", G)