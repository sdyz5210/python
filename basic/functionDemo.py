#!/usr/bin/python
# -*- coding: utf-8 -*-

def myfun(x,y):
	if x>y:
		return x
	else:
		return y

num = myfun(3,5)
print 'num=',num

def myfunc(x,y):
	return x+y,x*y

s1,s2 = myfunc(4,5)
print '函数返回值s1:',s1
print '函数返回值s2:',s2

no = [1,2,3,4,5,6]
def calc(*numbers):
	sum = 0;
	for number in numbers:
		sum = sum+number
	return sum
total = calc(*no)
print total
