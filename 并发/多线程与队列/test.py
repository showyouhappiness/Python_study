import threading
from queue import Queue


# 定义生产者函数
def producer(queue, items):
    for item in items:
        # 生产者向队列中放入数据
        queue.put(item)


# 定义消费者函数
def consumer(queue):
    while True:
        item = queue.get()
        # 消费者从队列中取出数据并进行处理
        print("Consumed:", item)
        queue.task_done()


# 创建队列
queue = Queue()

# 创建生产者线程并启动
producer_thread = threading.Thread(target=producer, args=(queue, [1, 2, 3, 4, 5]))
producer_thread.start()

# 创建消费者线程并启动
consumer_thread = threading.Thread(target=consumer, args=(queue,))
consumer_thread.start()

# 阻塞主线程，等待队列中的任务完成
queue.join()

# 输出：
# Consumed: 1
# Consumed: 2
# Consumed: 3
# Consumed: 4
# Consumed: 5
