name_list = ['zhangsan', 'lisi', 'wangwu']

# 取值和取索引
print(name_list[0])
print(name_list.index('lisi'))

# 修改
name_list[1] = "李四"

# 增加

# append方法可以向列表的末尾添加数据
name_list.append("王小二")
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(2, "王麻子")
# extend方法可以把其他列表中的完整数据添加到当前列表的末尾
temp_list = ['你好', '世界']
name_list.extend(temp_list)
name_list.extend(['1', '2'])

print(name_list)

# 删除
# remove 方法可以从列表中删除指定的数据
name_list.remove('wangwu')
# pop 方法可以从列表中删除指定的索引值对应的数据，
# 如果没有指定则删除最后一项
name_list.pop(2)
name_list.pop()
# clear 可以清空列表
name_list.clear()

print(name_list)

# -----------------------------------------------------
name_list2 = ['张三', '李四', '王五']

# 使用del关键字(delete)删除列表元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法

del name_list2[1]

name = "小明"
del name
# 注意如果使用del关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了
# print(name)
print(name_list2)

# -----------------------------------------------------
name_list3 = ['张三', '李四', '王五', '张三']

# len(length 长度)函数可以统计列表中元素的总数
list_len = len(name_list3)
print("列表中包含 %d 个元素" % list_len)
# count 方法可以统计列表中某一个数据出现的次数
list_num = name_list3.count('张三')
print("张三出现了 %d 次" % list_num)

# 从列表中删除第一次出现的数据,如果数据不存在,程序会报错
name_list3.remove("张三")
print(name_list3)

# -----------------------------------------------------
name_list4 = ['zhangsan', 'lisi', 'wangwu', 'wangxiaoer']
num_list = [6, 8, 4, 1, 10]
# 升序
name_list4.sort()
num_list.sort()
print(name_list4, num_list)
# 降序
name_list4.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list4, num_list)
# 反转
name_list4.reverse()
num_list.reverse()
print(name_list4, num_list)
