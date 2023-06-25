from multiprocessing import Process, Queue
import os, time, random


def download(q):
    for image in ['1.png', '2.png', '3.png']:
        print('正在下载：{}'.format(image))
        time.sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功!'.format(file))
        except:
            print('保存完毕')
            break


if __name__ == '__main__':
    q = Queue(5)  # 最多放5个数据，超过5个就会阻塞
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()  # 如果不加 那么p1执行完之后就清除了，所以需要等待

    p2.start()
    p2.join()

    print('程序结束！！！')
