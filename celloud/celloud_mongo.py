#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client.task
collection = db.taskTracing

def readInput(inputFile):
	newlines = []
	with open(inputFile,"r") as f:
		lines = f.readlines()
		#(creationTime,startTime,endTime)=null
		for line in lines:
			fileName = line.strip().split(",")[0]
			dataKey = line.strip().split(",")[1]
			taskId = line.strip().split(",")[2]
			(creationTime,startTime,endTime) = findTasks(taskId)
			newlines.append(line.strip()+","+creationTime+","+startTime+","+endTime+"\n")
		writeOutput("data_2.txt",newlines)

def writeOutput(outputFile,lines):
	with open(outputFile,'a') as f:
		for line in lines:
			f.write(line)
			f.flush()

def findTasks(taskId):
	task = collection.find_one({"taskId":int(taskId),"message":"收到bc回调，将任务投递到rgs"})
	return task['variables']['creationTime'],task['variables']['startTime'],task['variables']['endTime']
	
if __name__ == '__main__':
	inputFile = "data_1.txt"
	readInput(inputFile)