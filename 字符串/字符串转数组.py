str = '123,456'
list = str.split(',', )
list = [int(list[0]), int(list[1])]
print(list)
print('-'*50)
str1 = '3,5,6'
list_str = [int(v) for v in str1.replace(',', '')]
print(list_str)

str2 = '1,2,3'
arr = [int(v) for v in str2.split(',')]
print(arr)
