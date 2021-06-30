"""
局部变量
将定义在外边的全局变量放在循环里面形成局部变量
放在循环外面，只初始化了一次，意外着是一个对象，
不管循环多少次都是修改的同一个对象。
只是将同一个对象加入到数组N次。
"""
body_id = 1  # 编号从1开始
bodies = {}
# User_Information = {}  # 用户基本信息字典  之前是在这块，形成全局变量
while 1:
    User_Information = {}  # 用户基本信息字典
    name = input("请输入姓名: ")  # 输入姓名
    weight = int(input("请输入体重(单位Kg): "))  # 输入体重
    height = int(input("请输入身高(单位CM): "))  # 输入身高
    BMI = weight / (height / 100) ** 2  # 计算BMI值
    User_Information["name"] = name  # 录入姓名 str
    User_Information["weight"] = weight  # 录入体重 int
    User_Information["height"] = height  # 录入身高 int
    User_Information["BMI"] = BMI  # 录入BMI  Float
    print(User_Information)
    bodies[body_id] = User_Information  # ID对应用户基本信息
    print(bodies)
    Keep_on = input("是否继续输入(Y/N): ")
    if Keep_on.upper() == "Y":
        body_id += 1
    else:
        break
print(bodies)

print("*" * 50)

import collections
import numpy as np

a = np.array(([1, 2], [3, 4]))
c = collections.OrderedDict()

for i in range(a.shape[0]):
    b = collections.OrderedDict()  # 局部变量
    b['x'] = a[i][0]
    b['y'] = a[i][1]
    c[str(i)] = b
for key, value in c.items():
    print(id(c[key]))
    print(key, value)

print("*" * 50)

"""
深拷贝
使用了全局变量，但是通过深拷贝形成了一个新的地址
一般全局变量共用一个地址，如果将这个全局变量当做参数
那么就会造成第二个字典项的value覆盖第一个字典项的value
"""
import collections
import numpy as np

a = np.array(([1, 2], [3, 4], [5, 6], [7, 8]))
c = collections.OrderedDict()
b = collections.OrderedDict()
for i in range(a.shape[0]):
    b['x'] = a[i][0]
    b['y'] = a[i][1]
    print("b", b)
    c[str(i)] = b.copy()
    print("c", c)
print(id(b), id(c[str(0)]), id(b), id(c[str(1)]))
for key, value in c.items():
    print(id(c[key]))
    print(key, value)

body_id = 1  # 编号从1开始
User_Information = {}  # 用户基本信息字典
bodies = {}
while 1:
    name = input("请输入姓名: ")  # 输入姓名
    weight = int(input("请输入体重(单位Kg): "))  # 输入体重
    height = int(input("请输入身高(单位CM): "))  # 输入身高
    BMI = weight / (height / 100) ** 2  # 计算BMI值
    User_Information["name"] = name  # 录入姓名 str
    User_Information["weight"] = weight  # 录入体重 int
    User_Information["height"] = height  # 录入身高 int
    User_Information["BMI"] = BMI  # 录入BMI  Float
    bodies[body_id] = User_Information  # ID对应用户基本信息
    Keep_on = input("是否继续输入(Y/N): ")
    if Keep_on.upper() == "Y":
        body_id += 1
    else:
        break
print(bodies)
