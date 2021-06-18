day_t = {'u': 'tuesday', 'h': 'thursday'}
day_s = {'a': 'saturday', 'u': 'sunday'}
day = {'t': day_t, 's': day_s, 'm': 'monday', 'w': 'wednesday', 'f': 'friday'}
a = input('请输入第一个字母 \n')
if a in day.keys():
    print(day[a])
    if a == 't' or a == 's':
        b = input('请输入第二个字母 \n')
        if a == 't' and b in day_t.keys():
            print(day_t[b])
        if a == 's' and b in day_s.keys():
            print(day_s[b])
else:
    print('没有找到你输入的日期')
