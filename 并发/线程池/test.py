from concurrent.futures import ThreadPoolExecutor


def test(a, b):
    print(a, b)


qq = {"a": "1", "b": "2", "c": "3"}
with ThreadPoolExecutor() as pool:
    for j, k in qq.items():
        res = pool.submit(test, j, k)
        last = res.result()
