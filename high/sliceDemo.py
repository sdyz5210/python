#!/usr/bin/python
# -*- coding: utf-8 -*-

classmates = ['Tom','Jack','Lucy','Merry','John']
print '打印classmates列表',classmates
print '打印classmates列表中前三个元素',classmates[0:3]
print '打印classmates列表中1:4的元素',classmates[1:4]
#python支持索引为负数
print '打印classmates列表中后三个元素',classmates[-3:]
print '打印classmates列表中-2：-1的元素',classmates[-2:-1]

str='hello world!'
print '字符串的切片',str[3:8]