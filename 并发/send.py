def num():
    a = yield 1
    while True:
        a = yield a


c = num()
# print(c.send(None))  # 作用同下  返回生成器的第一个值
print(next(c))

print(c.send(5))
