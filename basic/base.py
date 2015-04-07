#!/usr/bin/python
# -*- coding: utf-8 -*-
print '------------------分支语句------------'
num = input('please enter one number:')
if num > 60 :
	print '及格了'
else:
	print '不及格'

print '------------------格式化--------------'
print '---------------格式化字符串------------'
print 'Hello,%s' % 'world'
print 'Hi,%s,you have $%d.' %('summer',1000)