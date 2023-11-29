import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('data.csv')

# 查看数据的前几行
print(data.head())

# 数据清洗和预处理
# 处理缺失值
data.dropna(inplace=True)

# 数据分析
# 描述性统计
print(data.describe())

# 数据可视化
# 绘制散点图
plt.scatter(data['age'], data['money'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of x vs y')
plt.show()