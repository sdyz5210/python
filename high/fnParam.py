#!/usr/bin/python
# -*- coding: utf-8 -*-

#正常情况下求和
def calc_sum(*args):
	sum = 0
	for x in args:
		sum = sum + x
	return sum

def lazy_sum(*args):
	def sum():
		ax = 0
		for x in args:
			ax = ax+x
		return ax
	return sum

f = lazy_sum(1,2,3,4)
print '打印f=',f
print '打印f()=',f()