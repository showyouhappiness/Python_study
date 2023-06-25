from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 设置进程池的数量为4
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # apply_async()方法用来向进程池提交需要执行的函数和参数，它会立即返回，不阻塞等待子进程的执行结果
    print('Waiting for all subprocesses done...')
    p.close()  # 调用close()之后就不能继续添加新的Process了
    p.join()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了，等待所有子进程执行完毕
    print('All subprocesses done.')
