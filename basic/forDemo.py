#!/usr/bin/python
# -*- coding: utf-8 -*-

print '今天我们学习：%s' % '循环语句'

#第一种循环
print '-------------------for------------------'
classmates = ['Tom','Jack','John','merry']
for classmate in classmates:
	print classmate

sum = 0
for x in xrange(1,10):
	sum +=x
print '累计和为 sum =',sum
print '生成序列range(10)'
num = range(10)
print '打印生成序列range(10)',num

print '-------------------while---------------'

n = 0
while sum > 0:
	sum-=5
	n+=1
print '本次循环次数为:',n

print '-----------------raw_input-------------'
str = int(raw_input('请输入:'))
print str
