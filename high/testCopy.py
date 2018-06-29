#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

import copy

a = [1,2,3,4,5,['a','b','c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(6)
a[5].append('d')

'''
赋值：a和b都指向同一对象
浅拷贝：对象的浅拷贝会为外层list分配新的内存空间，嵌套内存地址不变
深拷贝：所有的内存地址都会有变化
'''

print "a=",a
print "b=",b
print "c=",c
print "d=",d