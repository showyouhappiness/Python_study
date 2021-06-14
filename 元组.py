"""
元组和列表(数组)类似,不同之处在于元组的元素不能修改
    元组表示多个元素组成的序列
    元组在python开发中,有特定的应用场景
用于存储一串信息,数据之间使用,分隔
元组用()定义,列表用[]定义
元组的索引从0开始
"""
# 定义一个元组
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")
# 定义一个空元组
# 但是没有意义因为里面的元素不能修改一般情况下不会定义
info_tuple1 = ()
# 元组中只包含一个元素时,需要在元素后面添加逗号
info_tuple2 = (50, )

type(info_tuple)
type(info_tuple1)
type(info_tuple2)


# ------------------------------------------------
# 元组的使用方法
# 取值和取索引
print(info_tuple[0], info_tuple[1], info_tuple[2])
print(info_tuple.index("zhangsan"))

# 统计计数
print(info_tuple.count("zhangsan"))

# 统计元组中包含元素的个数
print(len(info_tuple))

for my_info in info_tuple:
    print(my_info)


# ----------------------------------------------------
# 元组与列表的互换
"""
使用list函数可以把元组转换成列表
list(元组)
使用tuple函数可以把列表转换成元组
tuple(列表)
"""
num_list = [1, 2, 3, 4]
type(num_list)
num_tuple = tuple(num_list)
type(num_tuple)
num_list2 = list(num_tuple)
type(num_list2)
