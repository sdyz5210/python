#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

def test1(count):
	count = count + 1
	if count==5:
			i = 10/(count-5)
	return count

def task():
	count = 0
	while True:
		try:
			count = test1(count)
		except Exception, e:
			raise e
		print count
		if count==10:
			break
task()