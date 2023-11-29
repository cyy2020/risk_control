import pandas as pd


df = pd.read_csv("data.csv")
print(df)
print(df.isna())  # 判断各元素是否缺失
print(df.isna().mean())  # 计算各列缺失比例
print(df[df.notna().all(axis=1)])  # 筛选均不为缺失值的记录
print(df.fillna(0))  # 常数填充
print(df.fillna(df.B.mean()))  # 均值填充
print(df.fillna(method='ffill'))  # 前向填充
print(df.fillna(method='bfill'))
