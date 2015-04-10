#!/usr/bin/python
# -*- coding: utf-8 -*-

#定义动物类
class Animal(object):
	pass

#定义会跑得
class Runnable(object):
	def run(self):
		print 'running……'

#定义会飞的
class Flyable():
	def fly(self):
		print 'Flying……'

#定义哺乳类
class Mammal(Animal):
	pass

#定义鸟类
class Bird(Animal):
	pass

class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Flyable):
	pass