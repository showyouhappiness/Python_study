import os
import queue
import threading
import time

q = queue.Queue()
path = r'E:\result_images1'


def read_file(file):
    with open(os.path.join(path, file), 'r') as f:
        q.put(f)
    return q


class ReadThread(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)  # super(ReadThread, self).__init__()
        self.file = file
        self.run()

    def run(self):
        self.res = read_file(self.file)

    def get_result(self):
        # 注：此方法特别慢
        return self.res


start = time.time()

threads = []
for file in os.listdir(path):
    t = ReadThread(file)
    time.sleep(0.05)
    threads.append(t)

[t.start() for t in threads]
[t.join() for t in threads]
for t in threads:
    result = t.get_result()

print("read time:", time.time() - start)
