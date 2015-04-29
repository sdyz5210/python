#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
class Mysql:

	def __init__(self,host,user,password,db,port=3306,charset='utf8'):
		self.host=host
		self.port=port
		self.user=user
		self.db = db
		self.password=password
		self.charset=charset
		try:
			self.conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db)
			self.conn.set_character_set(self.charset)
			self.cursor=self.conn.cursor()
		except Exception, e:
			raise e
			#print 'Mysql Error %d: %s' % (e.args[0],e.args[1])

	def query(self,sql):
		return self.cursor.execute(sql)

	def show(self):
		return self.cursor.fetchall()

	def __del__(self):
		self.cursor.close()
		self.conn.close()

if __name__ == '__main__':
	mysql = Mysql('localhost','root','novacloud','hospital')
	mysql.query('select * from tb_user')
	data = mysql.show()
	for x in data:
		print x[1]


