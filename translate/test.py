#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

def test1():
	content="你好"
	if isinstance(content, unicode):
		content = content.encode("utf-8")
	print content

def test2():
	for i in range(10):
		(b,result) = test3(i)
		print i,b

def test3(a):
	b = 0
	result = True
	try:
		b = a/(a-5)
	except Exception, e:
		print e
		result = False
		b = 1000
	return (b,result)

def readFileList():
	for i in range(1,13):
		(b,result) = test3(i)
		print b

if __name__ == '__main__':
	readFileList()