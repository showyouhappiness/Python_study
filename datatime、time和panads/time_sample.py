"""
time模块中时间表现的格式主要有三种：
a、timestamp时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
b、struct_time时间元组，共有九个元素组。
c、format time 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式

"""
import time

# 生成timestamp
print(time.time())  # 时间戳时间
print(time.localtime())  # 生成struct_time
print(time.strptime('2021-08-10 16:37:06', '%Y-%m-%d %X'))  # 格式化时间转struct_time
print(time.strftime("%Y-%m-%d %X", time.localtime()))  # struct_time转格式化时间

# 还有常用休眠time.sleep
time.sleep(2)
