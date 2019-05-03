#!/usr/bin/env python
# -*- coding:utf-8 -*-


import MySQLdb

"""
try:

    # connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
    # 这只是连接到了数据库，要想操作数据库需要创建游标。
    conn = MySQLdb.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123.cn',
        db = 'abc',
        )

    # 通过获取到的数据库连接conn下的cursor()方法来创建游标。
    cursor = conn.cursor()

    sql = "select * from test"

    #通过游标cursor操作execute()方法可以写入纯SQL语句。
    #增删改查都可以使用execute方法。
    cursor.execute(sql)
    for i in cursor.fetchall():
        print(i)

except Exception as e:
    print("Connection Error:" + str(e))
finally:
    conn.close()
"""

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123.cn',
    db='abc',
)

#通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()

#创建数据表,通过游标cur 操作execute()方法可以写入纯sql语句。
# 通过execute()方法中写如sql语句来对数据进行操作
#创建数据表,通过游标cur 操作execute()方法可以写入纯sql语句。
# 通过execute()方法中写如sql语句来对数据进行操作
# cur.execute("create table student(id int,name varchar(20),class varchar(30),\
# age varchar(10))")
#
# 插入一条数据
# a = "insert into student values('2','Tom',\
#  '3 year 2 class','9')"
# cur.execute(a)

# b = ("select * from student")
# cur.execute(b)
#修改查询条件的数据


c = ("update student set class='3 year 1 class' where name='Tom'")
cur.execute(c)
for i in cur.fetchall():
        print(i)
#



cur.close()    #cur.close() 关闭游标

conn.commit()
# conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，
# 否则数据不会被真正的插入。
#
conn.close()   #conn.close()关闭数据库连接
