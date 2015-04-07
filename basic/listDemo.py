#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding() 

print '今天我们学习：%s' % '可变数组list'
classmates = ['Tom','John','Lili','merry']
print '输出数组',classmates
print '输出数组的长度:',len(classmates)
print '输出数组中的第2个元素:',classmates[1]
print '-------------数组(增加)元素----------------'
print '输出数组中倒数第一个元素:',classmates[-1]
print '给数组追加一个元素: Lucy'
classmates.append('Lucy')
print '输出数组',classmates
print '为数组制定位置  1  处插入一个元素:Jack'
classmates.insert(1,'Jack')
print '输出数组',classmates
print '-------------数组(删除)元素----------------'
print '删除末尾的元素'
classmates.pop()
print '输出数组',classmates
print '删除指定位置为 2 的元素'
classmates.pop(2)
print '输出数组',classmates
print '-------------数组元素(替换)----------------'
print '把索引为 2 的Lili替换成Sari'
classmates[2] = 'Sari'
print '输出数组',classmates
print '-------------数组元素(另外形式)----------------'
gender = ['male','female']
county = ['china','english','janpan']
print 'gender数组为',gender
print 'county数组为',county
collect = [gender,county,32,13,'more']
print '输出多维数组',collect
print '输出多维数据的长度',len(collect)
print '-------------数组元素(中文形式)----------------'
hanzi = ['汉字']
#下面的输出结果很有意思，中文在list中显示时是不正常的，但是直接输出中文元素又是正常的
print '中文数组:', hanzi
print '中文数组元素:',hanzi[0]
