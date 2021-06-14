"""
字典:通常用于存储描述一个物体的相关信息

和列表的区别:
列表是有序的对象集合
字典是无须的对象集合

字典用{}定义

字典使用键值对存储数据,键值对之间使用,分割

键(key):索引
值(value):数据
键和值之间使用:分隔
键必须是唯一的
值可以取任何数据类型,但是键只能使用字符串,数字或元组

xiaoming = {
    "name":"小明",
    "age":18,
    "gender": True,
    "height": 1.75
}

"""
# 字典是一个无序的数据集合,
# 使用print函数输出字典时,通常输出的顺序和定义的顺序不一致
xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75
}
print(xiaoming)

# 取值
print(xiaoming["name"])

# 增加/修改
# 如果key不存在,会新增键值对
xiaoming["weight"] = 80
# 如果key存在,会修改已经存在的键值对
xiaoming["age"] = 20
print(xiaoming)

# 删除
xiaoming.pop("name")

print(xiaoming)


# ------------------------------------------
xiaoming_dict = {"name": "小明",
                 "age": 18}
# 统计键值对数量
print(len(xiaoming_dict))


# 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 注意:如果被合并的字典中包含已经存在的键值对,会覆盖原有的键值对
xiaoming_dict.update(temp_dict)

# 清空字典
xiaoming_dict.clear()

# -------------------------------------------------
# 迭代遍历字典
# 遍历K时每一次循环中,获取到的键值对的key

xiaoming_dict1 = {"name": "小明",
                  "qq": "123456",
                  "phone": "10086"}
for k in xiaoming_dict1:
    print("%s - %s" % (k, xiaoming_dict1[k]))


# ------------------------------------------------
"""
使用多个键值对,存储描述一个物更复杂体的数据信息
将多个字典放在一个列表中,再进行遍历
"""
card_list = [
    {"name": "张三",
     "qq": "123456",
     "phone": "10010"},
    {"name": "李四",
     "qq": "654321",
     "phone": "10086"},
]
for card_info in card_list:
    print(card_info)
    for k in card_info:
        print("%s - %s" % (k, card_info[k]))
