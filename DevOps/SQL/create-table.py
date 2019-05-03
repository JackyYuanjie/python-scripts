#!/usr/bin/python3
# -*- coding:utf-8 -*-

import MySQLdb

#打开数据库连接,unix_socket参数指定了sock文件的路径
db = MySQLdb.Connect(host="localhost",user="blog",passwd="123",db="blog",unix_socket='/data/services/lnmp/mysql5.7/logs/mysqld.sock')

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute()方法执行SQL，如果表存在则删除。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#使用预处理语句创建表:
SQL = """CREATE TABLE EMPLOYEE (
		FIRST_NAME CHAR(20) NOT NULL,
		LAST_NAME CHAR(20),
		AGE INT,
		SEX CHAR(1),
		INCOME FLOAT )"""

cursor.execute(SQL)

data = cursor.execute('show tables')

print("blog:{}".format(data))


#关闭数据库连接。
db.close()
