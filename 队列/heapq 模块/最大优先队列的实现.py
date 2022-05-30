import heapq


def largest_queue(arr):
    """
    最大优先队列的实现

    阅读 heapq 模块的源代码可以发现，其内置了最大优先队列的实现函数和操作函数，但没有内置新插入元素的函数
    """
    print("原数组：{0}".format(arr))
    # 将给定的列表转化为最大堆，线性时间
    heapq._heapify_max(arr)
    print("最大堆数组：{0}".format(arr))

    # 弹出最大元素
    item0 = heapq._heappop_max(arr)
    print("弹出的元素为：{0}".format(item0))
    print("弹出的元素后：{0}".format(arr))

    # 弹出最大元素，并插入一个新的元素
    item1 = heapq._heapreplace_max(arr, 9)
    print("弹出的元素为：{0}".format(item1))
    print("现在的堆结构为：{0}".format(arr))
