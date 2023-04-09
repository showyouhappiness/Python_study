# 测试代码
import time

log_path = "./2.txt"

with open(log_path, mode='a', encoding='utf8') as f1:
    while 1:
        f1.write("jjj\n")
        print("jjj")
        time.sleep(1)
        f1.flush()
