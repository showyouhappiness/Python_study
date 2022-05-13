# 导入numpy数据包
import numpy as np

# 创建一个ndarray数组
data1 = np.array(['美国队长', '钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠'])
data2 = np.array([['美国队长', '钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠'], ['灭霸', '奥创', '基利安', '卡西利亚斯', '冬兵']])
print(data1, type(data1))
print(data2, type(data2))
print('*' * 50)



'''
ndarray的索引和切片
'''
# 创建一个ndarray数组
n = np.arange(1, 50, 5)
print(n)
print(n[0])  # 索引
print(n[3])  # 索引
print(n[2:8])  # 切片
print(n[:5])  # 切片
print(n[6:])  # 切片

# 创建一个ndarray二位数组
n1 = np.arange(1, 13).reshape(4, 3)
print(n1)
print(n1[2, 1])
print(n1[:, 1])
print(n1[2, :])
print(n1[:, :2])

# arr[0]表示获取的是第一行的内容，只使用一个索引时，得到的结果为一行
print("arr[2]:", n1[2])

# 使用arr.T[0]表示获取的是第一列的内容
print("第2列的值为：", n1.T[2])

print('*' * 50)

'''

'''



