#!/usr/bin/python
# -*- coding: utf-8 -*-

#filter()也接收一个函数和一个序列

def is_odd(x):
	return x%2==1

f1 = filter(is_odd,range(1,11))
print '打印过滤后的列表',f1