#!/usr/bin/python
# -*- coding=utf-8 -*-
import time
import threading
import MySQLdb
import queue
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB


def mysql_connection():
    host = 'localhost'
    user = 'root'
    port = 3306
    password = '123456'
    db = 'test'
    charset = 'utf8'
    limit_count = 3  # 最低预启动数据库连接数量
    pool = PooledDB(MySQLdb, limit_count, maxconnections=15, host=host, user=user, port=port, passwd=password, db=db,
                    charset=charset,
                    use_unicode=True, cursorclass=DictCursor)
    return pool


def tread_connection_db(id):
    con = pool.connection()
    cur = con.cursor()
    sql = '''select id,name,age,weight from test where id = %s ''' % id
    cur.execute(sql)
    time.sleep(0.5)
    result = cur.fetchall()
    if result:
        print('this is tread %s (%s,%s,%s,%s)' % (
            id, result[0]['id'], result[0]['name'], result[0]['age'], result[0]['weight']))
    else:
        print('this tread %s result is none' % id)
    con.close()


if __name__ == '__main__':
    start = time.time()
    # 创建线程连接池，最大限制15个连接
    pool = mysql_connection()
    # 创建队列，队列的最大个数及限制线程个数
    q = queue.Queue(maxsize=10)
    # 测试数据，多线程查询数据库
    for id in range(50):
        # 创建线程并放入队列中
        t = threading.Thread(target=tread_connection_db, args=(id,))
        q.put(t)
        # 队列队满
        if q.qsize() == 10:
            # 用于记录线程，便于终止线程
            join_thread = []
            # 从对列取出线程并开始线程，直到队列为空
            while q.empty() != True:
                t = q.get()
                join_thread.append(t)
                t.start()
            # 终止上一次队满时里面的所有线程
            for t in join_thread:
                t.join()
    end = time.time() - start
    print(end)
