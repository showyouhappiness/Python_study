# 公共方法------------------------------------
# Python包含以下内置函数
# 如果是字典，只对key作比较
t_dict = {"a": "z", "b": "y", "c": "x"}
min(t_dict)  # 'a' z是最大的
max(t_dict)  # 'c' x是最小的

for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else下方的代码就不会被执行
    print("会执行吗？")
print("循环结束")

# for循环的完整用法
students = [
    {"name": "你好"},
    {"name": "世界"}
]

# 在学员列表中搜索指定的名字
find_name = "张三"

for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了%s" % find_name)
        # 如果已经找到了，直接退出循环，不再遍历后面的元素
        break
else:
    print("没有找到%s，请核对后再次查询" % find_name)
