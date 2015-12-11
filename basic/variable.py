#!/usr/bin/python
# -*- coding: utf-8 -*-

#测试动态变量

class Test():
	def __init__(self,**dic):
		self.name = "jon"
		for i in dic.keys():
			setattr(self,i,dic[i])

t = Test(a=1,b=2,c=3)
print t.a,t.b,t.c