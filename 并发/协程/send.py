def num():
    a = yield 1  # yield不但可以返回一个值，它还可以接收调用者发出的参数。
    print(a)
    a = yield a


c = num()
print(c.send(None))  # 作用同下  返回生成器的第一个值
# print(next(c))

print(c.send(5))
print(c.send(10))

# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
