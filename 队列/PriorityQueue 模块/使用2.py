import queue
import threading
import time

q = queue.PriorityQueue()
q.put([1, 'ace'])
q.put([40, 333])
q.put([3, 'afd'])
q.put([5, '4asdg'])
# 1是级别最高的，
while not q.empty():  # 不为空时候执行
    print(q.get())

q = queue.PriorityQueue()
q.put('我')
q.put('你')
q.put('他')
q.put('她')
q.put('ta')
while not q.empty():
    print(q.get())
