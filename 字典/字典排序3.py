dict = {'001375_Lef_0_result.jpg': 'Lef_0_result',
        '001375_Lef_2_result.jpg': 'Lef_2_result',
        '001375_Top_1_result': 'Top_1_result',
        '001375_Top_2_result.jpg': 'Top_2_result',
        '001375_Btm_0_result.jpg': 'Btm_0_result',
        '001375_Btm_2_result.jpg': 'Btm_2_result',
        '001375_Top_0_result.jpg': 'Top_0_result',
        '001375_Btm_1_result.jpg': 'Btm_1_result',
        '001375_Lef_1_result.jpg': 'Lef_1_result',
        }


def handle(key, sep_char='_'):
    ref_values = {'Top': '0', 'Lef': '1', 'Btm': '2'}
    pos = key.find(sep_char)
    print(ref_values[key[pos + 1:pos + 4]] + key[pos + 5:pos + 6])
    return ref_values[key[pos + 1:pos + 4]] + key[pos + 5:pos + 6]


sorted_keys = sorted(dict.keys(), key=handle)
print(sorted_keys)
dict2 = {key: dict[key] for key in sorted_keys}
print(dict2)
my_dict = {'a': 300, 'c': 100, 'b': 200}
list_1 = list(my_dict.items())
print(list_1, '11111111')
# 对字典按照key值进行排序,并返回排序后的新字典
my_dict_sortbykey = sorted(list_1, key=lambda x: x[0])
print(my_dict_sortbykey)
# 对字典按照values值 升序 进行排序,并返回排序后的新字典
my_dict_sortbykey = sorted(list_1, key=lambda x: x[1])
print(my_dict_sortbykey)
# 对字典按照values值 降序 进行排序,并返回排序后的新字典
my_dict_sortbykey = sorted(list_1, key=lambda x: x[1], reverse=True)
print(my_dict_sortbykey)
# 提取字典的所有keys并进行排序（实质就是sorted函数应用于简单元素的列表）
my_dict_sortedkeys = sorted(my_dict.keys())
print(my_dict_sortedkeys)
# 提取字典的所有values并进行排序（实质就是sorted函数应用于简单元素的列表）
my_dict_sortedvalues = sorted(my_dict.values())
print(my_dict_sortedvalues)
x = lambda a, b: a * b
print(x(5, 6))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
