import collections

dict2 = {'0_0_001375_Lef_0_resultNG.jpg': 'Lef_0_result',
         '0_0_001375_Lef_2_resultNG.jpg': 'Lef_2_result',
         '0_0_001375_Top_1_resultNG.jpg': 'Top_1_result',
         '0_0_001375_Top_2_resultNG.jpg': 'Top_2_result',
         '0_0_001375_Btm_0_resultNG.jpg': 'Btm_0_result',
         '0_0_001375_Btm_2_resultNG.jpg': 'Btm_2_result',
         '0_0_001375_Top_0_resultOK.jpg': 'Top_0_result',
         '0_0_001375_Btm_1_resultOK.jpg': 'Btm_1_result',
         '0_0_001375_Lef_1_resultOK.jpg': 'Lef_1_result',
         }


def handle(key, start_char='_'):
    ref_values = {'Top': '0', 'Lef': '1', 'Btm': '2'}
    pos = key.find(start_char, 8)
    print(ref_values[key[pos + 1:pos + 4]] + key[pos + 5:pos + 6])
    return ref_values[key[pos + 1:pos + 4]] + key[pos + 5:pos + 6]


sorted_keys = sorted(dict2.keys(), key=handle)
print(sorted_keys)
dict3 = {key: dict2[key] for key in sorted_keys}
print(dict3)

dict4 = collections.OrderedDict({key: dict2[key] for key in sorted(dict2.keys(), key=handle)})

print(dict4)

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(type(students[0]))
