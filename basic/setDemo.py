#!/usr/bin/python
# -*- coding: utf-8 -*-

s = set([1,2,3,4])
print s

s1 = set([1,1,3,3,4,5])
print 'set中不存在重复的',s1

s.add(5)
print 's增加一个元素',s

s2 = set([1,2,3])
s3 = set([4,5])
print 's2&s3',s2&s3
print 's2|s3',s2|s3

l = ['d','e','a','c']
print '打印list',l
l.sort()
print '打印排序后的list',l