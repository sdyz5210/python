#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import sqlite3

def test():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('select sqlite_version()')
		data = cur.fetchone()
		print 'SQLite version:%s' % data

def insert():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
		cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
		cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
		cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
		cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
		cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
		cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
		cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
		cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

def insertMany():
	cars = (
		(1, 'Audi', 52642),
		(2, 'Mercedes', 57127),
		(3, 'Skoda', 9000),
		(4, 'Volvo', 29000),
		(5, 'Bentley', 350000),
		(6, 'Hummer', 41400),
		(7, 'Volkswagen', 21600)
	)
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS Cars")
		cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
		cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

def readAll():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('select * from cars')
		rows = cur.fetchall()
		for row in rows:
			print row

def readByDict():
	con = sqlite3.connect('test.db')
	with con:
		con.row_factory = sqlite3.Row
		cur = con.cursor() 
		cur.execute('select * from cars')
		rows = cur.fetchall()
		for row in rows:
			print "%s %s %s" % (row["Id"], row["Name"], row["Price"])

def readAllOneByOne():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('select * from cars')
		#循环取出
		while True:
			row = cur.fetchone()
			if row == None:
				break
			print row[0],row[1],row[2]

def readOne():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('select * from cars')
		row = cur.fetchone()
		print row[0],row[1],row[2]

def update():
	uId = 1
	uPrice = 62300
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('UPDATE Cars SET Price=? WHERE Id=?',(uPrice, uId))
		con.commit()
		print "Number of rows updated: %d" % cur.rowcount

def update1():
	uId = 1
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('select Name,Price from Cars where Id=:Id',{"Id":uId})
		con.commit()
		row = cur.fetchone()
		print row[0],row[1]

def findMata():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute('PRAGMA table_info(Cars)')
		con.commit()
		row = cur.fetchall()
		for data in row:
			print data[0],data[1],data[2]

if __name__ == '__main__':
	#insertMany()
	#readAll()
	#readAllOneByOne()
	#readByDict()
	#update1()
	findMata()