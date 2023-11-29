import numpy as np

a = np.arange(12).reshape(-1, 3)
print(a)
print(np.delete(a, 0))