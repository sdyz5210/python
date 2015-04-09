#!/usr/bin/python
# -*- coding: utf-8 -*-

def f(x):
	return x*x

map1 = map(f,range(1,11))
print map1

#使用匿名函数实现
print '打印匿名函数运行结果',map(lambda x : x*x,range(1,11))