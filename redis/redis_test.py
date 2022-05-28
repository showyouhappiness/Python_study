import redis

'''
连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
'''
# 第一种连接方法：普通
redis_conn = redis.Redis(host='192.168.18.128', port=6379, password='crflyj', decode_responses=True)
# 第二种连接方法：连接池
# redis_pool = redis.ConnectionPool(host='192.168.18.128', port=6379, password='crflyj', decode_responses=True)
# redis_conn = redis.Redis(connection_pool=redis_pool)
# redis_conn.set('name', 'test2', ex=6, nx=True)
# print(redis_conn['name'])
# print(redis_conn.get('name'))  # 取出键name对应的值
# print(type(redis_conn.get('name')))
'''
pipeline
'''
# pipe = redis_conn.pipeline()  # 创建一个管道
# pipe.set('name', 'jack')
# pipe.set('role', 'sb')
# pipe.sadd('faz', 'baz')
# pipe.incr('num')  # 如果num不存在则vaule为1，如果存在，则value自增1
# pipe.execute()

# pipe.set('hello', 'redis').set('role', 'sb').sadd('faz', 'baz').incr('num').execute()
# print(redis_conn.get("hello"))
# print(redis_conn.get("role"))
# print(redis_conn.get("num"))

'''
geospatial
'''
# redis_conn.geoadd('city', 108.96, 34.26, 'xian', 116.40, 39.90, 'beijing', 121.47, 31.23, 'shanghai', 114.05, 22.52,
#                   'shenzhen')
#
# print(redis_conn.geopos('city', 'xian'))
# print(redis_conn.geodist('city', 'xian', 'beijing', 'km'))
# print(redis_conn.georadius('city', 108.96, 34.26, 1000, 'km'))
# print(redis_conn.georadius('city', 108.96, 34.26, 1000, 'km', withdist=True))
# print(redis_conn.georadius('city', 108.96, 34.26, 1000, 'km', withcoord=True))
# print(redis_conn.georadius('city', 108.96, 34.26, 1000, 'km', withdist=True, withcoord=True, count=1))
# print(redis_conn.georadiusbymember('city', 'beijing', 1000, 'km'))
# print(redis_conn.zrange('city', 0, -1))
# print(redis_conn.zrem('city', 'xian'))
# print(redis_conn.zrange('city', 0, -1))

'''
hyperloglog
'''
redis_conn.pfadd('A', 1, 2, 3, 4, 2, 2, 3, 4, 5)
redis_conn.pfadd('B', 3, 2, 3, 4, 4, 2, 3, 4)
redis_conn.pfmerge('C', 'A', 'B')
print(redis_conn.pfcount('C'))

'''
bitmaps
'''
# redis_conn.setbit('sign', 0, 1)
# redis_conn.setbit('sign', 1, 0)
# redis_conn.setbit('sign', 2, 0)
# redis_conn.setbit('sign', 3, 1)
# redis_conn.setbit('sign', 4, 1)
# redis_conn.setbit('sign', 5, 0)
# redis_conn.setbit('sign', 6, 0)

# print(redis_conn.getbit('sign', 3))
# print(redis_conn.getbit('sign', 6))

# print(redis_conn.bitcount('sign'))
