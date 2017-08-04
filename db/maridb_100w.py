#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def insert_10w():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','study')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	try:
		for i in range(100000):
			sql = "insert into tb_user(username,password,email,age,price,state) values('test_"+str(i)+"','123456','test_"+str(i)+"@126.com',25,12.4,0)"
			cursor.execute(sql)
			db.commit()
	except Exception, e:
		db.rollback()
		raise e
	finally:
		#关闭数据库连接
		db.close() 

insert_10w()