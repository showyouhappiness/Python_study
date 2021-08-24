array = ['abced', 'fghi', 'qwert', 'plmkij', 'majiangboqqqq']


def hasStr(str):
    return str.find('majiangbo') != -1


print(list(map(hasStr, array)).count(bool(True)))
print(list(map(hasStr, array)))

str = 'majiangbo'

for i in array:
    if str in i:
        print(True)
    else:
        print(False)
