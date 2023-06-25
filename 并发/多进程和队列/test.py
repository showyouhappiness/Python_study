from multiprocessing import Process, Queue


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
        if item is None:
            break
        print("Consumed:", item)


if __name__ == '__main__':
    # 创建队列
    queue = Queue()

    # 创建生产者进程并启动
    producer_process = Process(target=producer, args=(queue, [1, 2, 3, 4, 5]))
    producer_process.start()

    # 创建消费者进程并启动
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()

    # 等待生产者进程完成
    producer_process.join()

    # 向队列发送结束信号，让消费者进程结束，否则造成死锁
    queue.put(None)

    # 等待消费者进程完成
    consumer_process.join()

    # 输出：
    # Consumed: 1
    # Consumed: 2
    # Consumed: 3
    # Consumed: 4
    # Consumed: 5
