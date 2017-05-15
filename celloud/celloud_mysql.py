#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def readInput(inputFile):
	newlines = []
	with open(inputFile,"r") as f:
		lines = f.readlines()
		for line in lines:
			fileName = line.split(",")[0]
			dataKey = line.split(",")[1]
			result = getTaskId(dataKey)
			newlines.append(line.strip()+","+str(result)+"\n")
		writeOutput("data_1.txt",newlines)

def writeOutput(outputFile,lines):
	with open(outputFile,'a') as f:
		for line in lines:
			f.write(line)
			f.flush()

def getTaskId(dataKey):
	#打开数据库连接
	db = MySQLdb.connect('localhost','root','password','dbName')
	#获取操作游标
	cursor = db.cursor()
	#执行sql语句
	sql = 'select task_id from tb_task where data_key='+dataKey
	try:
		cursor.execute(sql)
		result = cursor.fetchone()
		return result[0]
	except Exception, e:
		db.rollback()
		raise e
	finally:
		#关闭数据库连接
		db.close() 

if __name__ == '__main__':
	inputFile = "data.txt"
	#第一步
	#readInput(inputFile)
	