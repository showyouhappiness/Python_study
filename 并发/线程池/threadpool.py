# import time
#
#
# def sayhello(str):
#     print("Hello ", str)
#     time.sleep(2)
#
#
# name_list = ['xiaozi', 'aa', 'bb', 'cc']
# start_time = time.time()
# for i in range(len(name_list)):
#     sayhello(name_list[i])
# print('%d second' % (time.time() - start_time))

# coding: utf-8
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED
import time


def spider(page):
    print(f"crawl task{page} finished")
    return page


list1 = ['30006', '30008', '30010']
start_time = time.time()
with ThreadPoolExecutor(max_workers=100) as t:
    all_task = [t.submit(spider, page) for page in range(1, 10000)]
    wait(all_task, return_when=ALL_COMPLETED)
    print('finished')
    print(time.time())

for i in range(1, 10000):
    spider(i)
print(start_time)
print(time.time())

# https://www.jianshu.com/p/6d6e4f745c27
