import os
import queue
import threading
import time

q = queue.Queue()
path = r'E:\result_images1'


def read_file(file):
    with open(os.path.join(path, file), 'r') as f:
        q.put(f)


start = time.time()

threads = []
for file in os.listdir(path):
    t = threading.Thread(target=read_file, args=(file,))
    time.sleep(0.05)
    threads.append(t)

[t.start() for t in threads]
# [t.join() for t in threads]

while not q.empty():
    q.get()
    q.task_done()

print("read time:", time.time() - start)
