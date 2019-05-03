#!/usr/bin/python3

import MySQLdb

#打开数据库连接,unix_socket参数指定了sock文件的路径
db = MySQLdb.Connect(host="localhost",user="blog",passwd="123",db="blog",unix_socket='/data/services/lnmp/mysql5.7/logs/mysqld.sock')

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")

#使用fetchone()方法获取单条数据。
data = cursor.fetchone()

print("Database version:{}".format(data))


#关闭数据库连接。
db.close()
