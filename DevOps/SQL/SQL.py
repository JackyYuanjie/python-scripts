#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

"""
conn = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd='',
	db = 'test',
	)

cursor = conn.cursor()
sql = "create table user(id int,name varchar(30),password varchar(30))"
cursor.execute(sql)

sql = "insert into user(id,name,password) values('1','xiaoming','123456')"
cursor.execute(sql)

conn.commit()
cursor.execute('show tables')
cursor.execute('select * from user')
cursor.fetchall()
conn.close()
"""

class Mysql(object):
	def __init__(self):
		try:
			self.conn = pymysql.connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				passwd='xxx',
				db = 'test',
			)
		except Exception as e:
			print(e)
		else:
			print('连接成功')
			self.cur = self.conn.cursor()


	# def create_table(self):   #创建表
	# 	sql =''
	# 	res = self.cur.execute(sql)
	# 	print(res)



	def add(self):  #增加数据
		sql = '
		res = self.cur.execute(sql)
		if res:
			self.conn.commit()
		else:
			self.conn.rollback()
		print(res)


	def rem(self):  #删除数据
		sql = ''
		res = self.cur.execute(sql)
		if res:
			self.conn.commit()
		else:
			self.conn.rollback()
		print(res)

	def mod(self):  #更改数据
		sql = ''
		res = self.cur.execute(sql)
		if res:
			self.conn.commit()
		else:
			self.conn.rollback()
		print(res)


	def show(self):
		sql = ''
		self.cur.execute(sql)
		res = self.cur.fetchall()
		for i in res:
			print(i)

	def close(self):   #关闭
		self.cur.close()
		self.conn.close()

if __name__=="__main__":
	mysql = Mysql()
	# mysql.create_table()
	# mysql.add()
	# mysql.mod()
	# mysql.rem()
	# mysql.show()
	# mysql.close()
