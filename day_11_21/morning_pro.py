"""
# 1.2 功能
创建n维数组(矩阵)
对数组进行函数运算，使用函数计算十分快速，节省了大量的时间，且不需要编写循环，十分方便
数值积分、线性代数运算、傅里叶变换
ndarray快速节省空间的多维数组，提供数组化的算术运算和高级的 广播功能。

# 1.3 对象
NumPy中的核心对象是ndarray
ndarray可以看成数组，存放 同类元素
NumPy里面所有的函数都是围绕ndarray展开的
ndarray 内部由以下内容组成：
一个指向数据(内存或内存映射文件中的一块数据)的指针。
数据类型或 dtype，描述在数组中的固定大小值的格子。
一个表示数组形状(shape)的元组，表示各维度大小的元组。形状为(row×col)

# 1.4 数据类型
numpy 支持的数据类型比 Python 内置的类型要多很多，基本上可以和C语言的数据类型对应上主要包括int8、int16、int32、int64、uint8、uint16、
uint32、uint64、float16、float32、float64

1.5 数组属性
属性    +      说明
# """
# import numpy as np
#
# lst = [1, 2, 3, 4]
# nd1 = np.array(lst)
# print(nd1, type(nd1))


# import numpy as np
#
# # 0到1标准正态分布
# arr1 = np.random.randn(3, 3)
# # 0到1均匀分布
# arr2 = np.random.rand(3, 3)
# # 均匀分布的随机数（浮点数），前两个参数表示随机数的范围，第三个表示生成随机数的个数
# arr3 = np.random.uniform(0, 10, 2)
# # 均匀分布的随机数（整数），前两个参数表示随机数的范围，第三个表示生成随机数的个数
# arr4 = np.random.randint(0, 10, 3)
# print(f'arr1 : {arr1}\narr2 : {arr2}\narr3 : {arr3}\narr4 : {arr4}')

import numpy as np

# # 未初始化的数组
# arr1 = np.empty((2, 3))
# # 数组元素以 0 来填充
# arr2 = np.zeros((2, 3))
# # 数组元素以 1 来填充
# arr3 = np.ones((2, 3))
# # 数组以指定的数来进行填充，这里举例3
# arr4 = np.full((2, 3), 3)
# # 生成单位，对角线上元素为 1，其他为0
# arr5 = np.eye(3)
# # 二维矩阵输出矩阵对角线的元素，一维矩阵形成一个以一维数组为对角线元素的矩阵
# arr6 = np.diag(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#
# arr7 = np.linspace(0, 1, 4)  # out : array([0.        , 0.33333333, 0.66666667, 1.        ])
# arr8 = np.arange(0, 9, 2)  # out : array([0, 2, 4, 6, 8])
#
# print(
#     f'arr1 : {arr1}\narr2 : {arr2}\narr3 : {arr3}\narr4 : {arr4}\narr5: {arr5}\narr6: {arr6}\narr7: {arr7}\narr8: {arr8}')

# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# rows = np.array([[0, 0], [3, 3]])  # 表示第1、4行
# cols = np.array([[0, 2], [0, 2]])  # 表示第1、3列
# # print(rows, cols)
# y = x[rows, cols]
# print(y)

# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x[x > 5])  # out : [ 6  7  8  9 10 11]
# b = x > 5
# print(b)

# a = np.array([2, 4, 6, 8, 10, 3]).reshape(2, 3)
# c = np.where(a > 5)  # 返回索引 out : (array([0, 1, 1], dtype=int64), array([2, 0, 1], dtype=int64))
# print(a[c])  # 获得元素

# x = np.arange(12).reshape(3, 4)
# # x.reshape(4, -1)
# print(x.reshape(2, -1))

# arr = np.arange(8).reshape(2, 4, 1)
# print(arr)
# print(arr.squeeze())

# arr = np.arange(12).reshape(2, 6, 1)
# print(arr)
# print(arr.transpose(1, 2, 0))

# arr = np.arange(20).reshape(4, 5)
# print(arr.swapaxes(1, 0))

# arr = np.random.choice([0, 3, 5, 7, 8, 9], p=[0.1, 0.1, 0.3, 0.2, 0.1, 0.2])
# print(arr)

a = np.random.randint(1, 20, size=(4, 5))  # 随机生成4行5列的数组
print(np.mean(a))  # 平均值
print(np.max(a))  # 最大值
print(np.min(a))  # 最小值
print(np.sum(a))  # 求和
print(np.prod(a))  # 求积
print(np.std(a))  # 求标准差
print(np.var(a))  # 求方差
print(np.median(a))  # 求中位数
print(np.argmax(a))  # 最大值索引
print(np.argmin(a))  # 最小值索引
