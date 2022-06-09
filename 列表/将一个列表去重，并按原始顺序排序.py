print(range(0, 20)[2:-2])

alist = [2, 5, 6, 3, 2, 6, 3, 2, 8]
new_list = list(set(alist))
new_list.sort(key=alist.index)
print(new_list)

