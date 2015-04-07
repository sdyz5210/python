#!/usr/bin/python
# -*- coding: utf-8 -*-

print '今天我们学习：%s' % '分支语句if'

score = input('请输入你的成绩')

if score > 90:
	print '您的等级为:','A'
elif score > 80:
	print '您的等级为:','B'
elif score > 70:
	print '您的等级为:','C'
elif score > 60:
	print '您的等级为:','D'
else:
	print '您的等级为:','E'


