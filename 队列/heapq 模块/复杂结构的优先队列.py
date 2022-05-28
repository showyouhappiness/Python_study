import heapq


def object_queue():
    """
    针对对象结构的优先队列
    """
    q = []
    heapq.heappush(q, (2, 'code'))
    heapq.heappush(q, (1, 'eat'))
    heapq.heappush(q, (3, 'sleep'))
    heapq.heappush(q, (2, 'play'))
    heapq.heappush(q, (3, "debug"))
    q1 = [x for x in q]
    while q:
        next_item = heapq.heappop(q)
        print(next_item)
    # ---- result -----
    # (1, 'eat')
    # (2, 'code')
    # (2, 'play')
    # (3, 'debug')
    # (3, 'sleep')

    # 返回最小的 n 个元素，相当于 sorted(iterable, key=key)[:n]
    n_smallest = heapq.nsmallest(3, q1, key=lambda x: x[0])
    print("最小的3个元素：{0}".format(n_smallest))
    # 返回最大的 n 个元素，相当于 sorted(iterable, key=key, reverse=True)[:n]
    n_largest = heapq.nlargest(3, q1, key=lambda x: x[1])
    print("最大的3个元素：{0}".format(n_largest))


object_queue()
