# 通过生成器完成4G内存读取5G数据
def get_lines():  # 生成器
    with open('../study/test.py', 'rb') as f:
        while True:
            data = f.readlines(100)
            if data:
                yield data
            else:
                break


f = get_lines()  # 迭代器对象
print(next(f))
print(next(f))
print(next(f))
