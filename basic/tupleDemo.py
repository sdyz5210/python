#!/usr/bin/python
# -*- coding: utf-8 -*-

#元组一旦初始化，就不可更改
print '今天我们学习：%s' % '元组tuple'
classmates = ('Tom','John','Lili','merry')
print '打印元组',classmates
print '打印元组的长度',len(classmates)
print '打印元组第2个元素',classmates[1]


print '-------------元组tuple中文---------------'
#定义一个元素的元组时需使用下列样式消除歧义
hanzi = ('汉字',)
#下面的输出结果很有意思，中文在list中显示时是不正常的，但是直接输出中文元素又是正常的
print '中文数组:', hanzi
print '中文数组元素:',hanzi[0]