import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.concatenate((x, y), axis=0)
print(z)

t = np.vstack((x, y))
print(t)

# p = np.hstack((x, y))
# print(p)
o = np.array([[99], [99]])
p = np.array([[1, 2, 3], [4, 5, 6]])

q = np.hstack((p, o))
print(q)

print('----------------------------')

x = np.array([1, 2, 3, 99, 99, 3, 2, 1])
print(x)

#等分为4份
x_split = np.split(x, 4)
print(x_split)

x = np.random.randint(10,size=(2,8))
print(x)

