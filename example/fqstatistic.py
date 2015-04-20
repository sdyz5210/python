#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os

'''
获取fq文件的长度统计
'''

if len(sys.argv) != 3:
	print 'Usage: *.py inputFile outputFile'
	sys.exit(0)
inputFile = sys.argv[1]
outputFile = sys.argv[2]

fileName = ''
totalReads = 0
totalTen = 0
maxTen = 0
minTen = 0

if os.path.isfile(inputFile):
	with open(inputFile,'r') as f:
		fileName = f.name
		line = f.readline()
		i = 1
		minTen = len(line)
		maxTen = len(line)
		while line:
			if i%4 ==2:
				if len(line)>maxTen:
					maxTen = len(line)
				if len(line)<minTen:
					minTen = len(line)
				totalTen = totalTen+len(line)
			line = f.readline()
			i = i+1
		totalReads = i/4
		#print 'fileName:%s,totalReads:%s,totalTen:%s,maxTen:%s,minTen:%s' % (f.name,totalReads,totalTen,maxTen,minTen)
else:
	print '您输入的不是一个文件'

with open(outputFile,'a') as fw:
		fw.write(fileName + ',' + (str)(totalReads) + ',' + (str)(totalTen) + ',' + (str)(maxTen) + ',' + (str)(minTen))