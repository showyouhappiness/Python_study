from multiprocessing import Process
import os
from time import sleep


# 子进程要执行的代码
def run_proc(name):
    sleep(1)
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步,如果没有这一句就会先执行下面再回头执行上面的子进程
    print('Child process end.')
