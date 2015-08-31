#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

#操作sqllite3
import sqlite3

def initDB():
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
		data = cur.fetchall()
		length = len(data)
		print length
		if length!=0:
			cur.execute("CREATE TABLE tb_file(id INT PRIMARY KEY NOT NULL, file_name TEXT, file_size INT,file_type TEXT,file_md5 TEXT,file_path TEXT)")

def insertFile(fd):
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cus.execute("insert into tb_file(file_name,file_size,file_type,file_md5,file_path) values(?,?,?,?,?)",(fd.fileName,fd.fileSize,fd.fileType,fd.fileMd5,fd.filePath))

def findOneFile(id):
	con = sqlite3.connect('test.db')
	with con:
		cur = con.cursor()
		cur.execute("select * from tb_file where id=:id",{"id":id})
		row = cur.fetchone()
		print row[0],row[1],row[2]