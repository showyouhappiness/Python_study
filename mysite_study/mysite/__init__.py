# 一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。
import pymysql
pymysql.version_info = (1, 4, 3, "final", 0)  # 修改版本号
pymysql.install_as_MySQLdb()  # 替换默认的数据库引擎
