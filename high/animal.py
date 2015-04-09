#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print 'Animal is running……'

class Dog(Animal):
	def run(self):
		print 'Dog is running……'

	def eat(self):
		print 'Dog is eating……'

class Cat(Animal):
	def run(self):
		print 'Cat is running……'


dog = Dog()
dog.run()
dog.eat()

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Cat())