import threading


class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)
        return self.result


# 示例函数，用于在线程中执行
def calculate_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum


# 创建线程实例并获取结果
start_num = 1
end_num = 1000000

thread = MyThread(calculate_sum, (start_num, end_num))
thread.start()

# 在此可以执行其他操作，同时线程在后台计算结果

# 获取线程结果
result = thread.get_result()
print(f"The sum from {start_num} to {end_num} is: {result}")
