arr = ['a', 'b']
str1 = ','.join(arr)
print(str1)

arr = [1, 2, 3]
str2 = ','.join(str(i) for i in arr)
print(str2)
