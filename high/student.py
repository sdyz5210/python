#!/usr/bin/python
# -*- coding: utf-8 -*-

#主要用于python中类的学习。封装。
class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s:%s' %(self.name,self.score)

	def get_grade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=80:
			return 'B'
		elif self.score>=70:
			return 'C'
		elif self.score>=60:
			return 'D'
		else:
			return 'E'

Tom = Student('Tom',90)
Jack = Student('Jack',80)

Tom.print_score()
Jack.print_score()

print 'Tom grade=',Tom.get_grade()