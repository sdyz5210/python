#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python v2.7.6

from pymongo import MongoClient

#在本机上运行，使用MongoClient()和MongoClient("localhost",27017)没有区别
client = MongoClient()
#client = MongoClient("localhost",27017)
#client = MongoClient("mongodb://localhost:27017/")

db = client.summer
#db = client[summer]

collection = db.user
#collection=db[user]

def printRecord():
	map = collection.find()
	for m in map:
		print "打印记录:",m

def printOneRecord():
	map=collection.find_one();
	for k,v in map.items():
		print "打印记录:",(k,v)


def printCount():
	count = collection.find().count()
	print "打印记录数:",count

def printInsertId():
	map={"name":"xia","age":20}
	id=collection.insert_one(map).inserted_id
	print "id:",id

def insertMoreRecord():
	map=[{"name":"lin","age":25},{"name":"qinger","age":23},{"name":"qiang","age":24}]
	collection.insert(map)

#insertMoreRecord()
printRecord()