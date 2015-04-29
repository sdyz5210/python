#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def test():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','hospital')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	cursor.execute('select version()')
	#获取一条数据
	data = cursor.fetchone()
	print 'Database version:%s' % data
	#关闭数据库连接
	db.close()

def createDb():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','hospital')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	cursor.execute('drop table if exists tb_test')
	sql = '''create table tb_test(
		username char(20) not null,
		age int,
		sex char(1)
		)'''
	cursor.execute(sql)
	#关闭数据库连接
	db.close() 

def insert():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','hospital')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	sql = '''insert into tb_test(username,age,sex) values('mac',20,'M')'''
	try:
		cursor.execute(sql)
		db.commit()
	except Exception, e:
		db.rollback()
		raise e
	finally:
		#关闭数据库连接
		db.close() 

def find():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','hospital')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	sql = 'select * from tb_test'
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			username = row[0]
			age = row[1]
			sex=row[2]
			print 'username=%s,age=%s,sex=%s' % (username,age,sex)
	except Exception, e:
		db.rollback()
		raise e
	finally:
		#关闭数据库连接
		db.close() 

def update():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','hospital')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	sql = "update tb_test set age=age+1 where sex='M'"
	try:
		cursor.execute(sql)
		db.commit()
	except Exception, e:
		db.rollback()
		raise e
	finally:
		#关闭数据库连接
		db.close() 

def delete():
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','novacloud','hospital')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	sql = "delete from tb_test where age=22"
	try:
		cursor.execute(sql)
		db.commit()
	except Exception, e:
		db.rollback()
		raise e
	finally:
		#关闭数据库连接
		db.close() 


#test()
#createDb()
#create()
#find()
#update()
#delete()