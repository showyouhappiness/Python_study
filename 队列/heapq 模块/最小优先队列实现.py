import heapq


def smallest_queue(arr):
    """
    默认为最小优先队列
    """
    print("原数组：{0}".format(arr))
    # 将给定的列表转化为最小堆，线性时间
    heapq.heapify(arr)
    print("最小堆数组：{0}".format(arr))

    # 插入元素
    heapq.heappush(arr, 5)
    print("插入新元素后：{0}".format(arr))

    # 弹出最小元素
    item0 = heapq.heappop(arr)
    print("弹出的元素后：{0}".format(item0))

    # 返回最小元素
    item1 = arr[0]
    print("获取最小元素的值：{0}".format(item1))

    # 弹出最小元素，并插入一个新的元素，相当于先 heappop, 再 heappush
    item2 = heapq.heapreplace(arr, -2)
    print("弹出的元素为：{0}".format(item2))
    print("现在的堆结构为：{0}".format(arr))


smallest_queue()
