#!/usr/bin/python
# -*- coding: utf-8 -*-

l1 = range(1,11)
print '打印数组',l1

#生成1*1，2*2……10*10
l2 = []
for x in xrange(1,11):
	l2.append(x*x)
print '打印数组',l2

l3 = [x*x for x in range(1,11)]
print '打印数组',l3

l4 = [x*x for x in range(1,11) if x%2==0]
print '打印数组',l4

l5 = [m+n for m in 'ABC' for n in 'XYZ']
print '打印数组',l5

# 导入os模块，模块的概念后面讲到
import os 
# os.listdir可以列出文件和目录
l6 = [d for d in os.listdir('.')] 
print '打印目录',l6