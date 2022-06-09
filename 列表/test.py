bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])

bicycles[0] = "自行车第一个元素";
print(bicycles)
bicycles[-1] = "自行车最后一个元素"
print(bicycles)
bicycles.append("飞机")
print(bicycles)
bicycles.insert(0, "替换第一个元素")
print(bicycles)
bicycles.insert(-1, "替换最后一个元素")
print(bicycles)

newBicycles = bicycles;
print(newBicycles)
newBicycles.insert(0, "我是0")
newBicycles.insert(-1, "我是-1")

print(newBicycles)

a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
b = [j for i in a for j in i if j > 3]
print(b)
