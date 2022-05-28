"""
数字队列优先级排序 正常的数字排序
"""
import queue as Q


def PriorityQueue_int():
    que = Q.PriorityQueue()
    que.put(10)
    que.put(1)
    que.put(5)
    while not que.empty():
        print(que.get())


PriorityQueue_int()
