#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):

	def get_score(self):
		return self._score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value >100:
			raise ValueError('score must between 1~100!')
		self._score = value

s = Student()
s.set_score(60)
print '分数=',s.get_score()

#下面代码执行会有问题
#s.set_score(600)
#使用property

class Person(object):
	@property
	def age(self):
		return self.__age

	#如果此处不定义age.setter,age属性就是一个只读属性
	@age.setter
	def age(self,age):
		if not isinstance(age,int):
			raise ValueError('age must be an integer!')
		if age < 0 or age >100:
			raise ValueError('age must between 1~100!')
		self.__age = age

p = Person()
p.age = 25
print 'age=',p.age