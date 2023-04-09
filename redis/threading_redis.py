import threading
import redis

data = []


def connect(ip):
    global data
    # 普通
    redis_conn = redis.Redis(host=ip, port=6379, password='1q2w3e4r5t', decode_responses=True)
    # 连接池
    # redis_pool = redis.ConnectionPool(host=ip, port=6379, password='1q2w3e4r5t', decode_responses=True)
    # redis_conn = redis.Redis(connection_pool=redis_pool)
    ps = redis_conn.pubsub()
    ps.subscribe('liao')  # 从liao订阅消息
    print(ip)
    for item in ps.listen():  # 监听状态：有消息发布了就拿过来
        if item['type'] == 'message':
            print(item['channel']+':'+ip)
            print(item['data'])


if __name__ == "__main__":
    # 设置共享list
    con = ["localhost", "127.0.0.1"]
    # 设置进程池大小
    th = []
    for i in con:
        p = threading.Thread(target=connect, args=(i,))
        th.append(p)
        p.start()
    for p in th:
        p.join()
