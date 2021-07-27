import psycopg2


# sql = '''CREATE database mydb''';
# # 创建数据库
# passwd.cur.execute(sql)
class passwd():
    conn = psycopg2.connect(database="testdb", user="postgres", password="l123456..", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT team  from users where player = '库里';")
    rows = cur.fetchall()
    for row in rows:
        passwd = row[0]
        print(passwd)
    conn.close()


if __name__ == '__main__':
    passwd = passwd
