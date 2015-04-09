#!/usr/bin/python
# -*- coding: utf-8 -*-

#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
print 'abs(10)=',abs(10)

f = abs
print 'f(-10)=',f(-10)

def test(x,y,f):
	return f(x) + f(y)
sum =test(-10,10,abs)
print 'sum =',sum
