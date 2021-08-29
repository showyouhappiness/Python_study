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


start = time.time()
pool = mysql_connection()

for id in range(50):
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

end = time.time() - start
print(end)
