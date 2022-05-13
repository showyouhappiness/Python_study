import json

key_list = []


def generate_file():
    with open('C:\\Users\\Administrator\\.crf-config.json', 'r') as f:
        read_result = json.loads(f.read())
        return read_result


def get_dict_allkeys(dict_a):
    """
    多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
    :param dict_a:
    :return: key_list
    """
    global key_father, temp_key_son
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
        temp_key = list(dict_a.keys())
        for key_father in temp_key:

            temp_value = dict_a[key_father]
            if isinstance(temp_value, dict):
                temp_key_son = list(temp_value.keys())

            for key_son in temp_key_son:
                key_name = 'self.' + str(key_father) + '_' + str(key_son)
                key_list.append(key_name)
    print(key_list)


get_dict_allkeys(generate_file())
