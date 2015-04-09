#!/usr/bin/python
# -*- coding: utf-8 -*-

#for 循环迭代list
l=range(10)
for x in l:
	print x

#for 循环dict  默认情况dict迭代的是key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key

#for 循环dict 迭代value
for value in d.itervalues():
	print value
#for 循环dict 迭代key,value
for k, v in d.iteritems():
	print k,'--',v

#for 循环迭代字符串
for ch in 'ABC':
	print ch