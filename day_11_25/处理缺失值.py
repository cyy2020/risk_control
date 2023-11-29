import numpy as np

# 创建示例数据集
data = np.array([[1, 2, 3, 4],
                 [5, 6, np.nan, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, np.nan]])

print(data)

# 计算每一列的均值
col_mean = np.nanmean(data, axis=0)
print(col_mean)

# 将缺失值替换为对应列的均值
inds = np.where(np.isnan(data))
print(inds)
print(inds[1])
data[inds] = np.take(col_mean, inds[1])

print("处理缺失值后的数据集：\n", data)
