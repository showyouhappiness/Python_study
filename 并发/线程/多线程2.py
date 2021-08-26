import time
from threading import Thread

test_data_dict = {}


def test(n):
    test_data_dict[n] = n


if __name__ == '__main__':
    test_data_dict.clear()
    ts = []

    start = time.time()
    for i in [1, 2, 3, 4, 5]:
        t = Thread(target=test, args=[i])
        ts.append(t)

    for i in ts:
        i.start()
        i.join()
    print(test_data_dict)
    print("read time:", time.time() - start)
