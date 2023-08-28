import csv

# 两个元组，每个元组内有多个值
tuple1 = ('apple', [1, 2, 3], {'name': 'Apple', 'color': 'red'})
tuple2 = ('apple', [1, 2, 3], {'name': 'Banana', 'color': 'yellow'})
data = [
    ['Name', 'Age', 'City']
]
data1 = []


# 比较元组内的内容是否一致，并打印不一致的内容
def compare_tuples(t1, t2):
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            data1.append([t1[i], t2[i]])
        else:
            data1.append('')

    data.append(data1)


# 调用比较函数
compare_tuples(tuple1, tuple2)

# 要生成的数据，每一行表示一个记录，每一行内的元素表示字段值

# 指定要生成的 CSV 文件的路径
file_path = 'output.csv'

# 使用 csv 模块写入数据到 CSV 文件
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # 逐行写入数据
    for row in data:
        writer.writerow(row)

print("CSV 文件已生成。")
