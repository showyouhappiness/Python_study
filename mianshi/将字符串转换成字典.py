str1 = "k:1|k1:2|k2:3|k3:4"


def str2dict(str):
    dict1 = {}
    for i in str.split('|'):
        key, value = i.split(':')
        dict1[key] = value
    return dict1


print(str2dict(str1))
