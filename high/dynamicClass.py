#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):
	pass

#动态增加属性
s = Student()
s.name = 'Tom'
print 's.name=',s.name

#动态绑定方法
def set_age(self,age):
	self.age = age

from types import MethodType

s.set_age = MethodType(set_age,s,Student)

s.set_age(25)

print 's.age =',s.age

s1 = Student()

#下面代码会出错，因为上面的绑定只针对s这个对象
#s1.set_age(30)
#print 's1.age =',s1.age
#为了解决上述问题，可以给所有实例绑定

Student.set_age = MethodType(set_age,None,Student)
s.set_age(30)
print 's.age =',s.age

s2 = Student()
s2.set_age(28)
print 's2.age = ',s2.age


#以上动态绑定的功能很变态，造成疯狂绑定没有任何限制
#使用slots进行绑定,例如下面

class Person(object):
	__slots__ = ('name','age')

p = Person()
p.name = 'Jack'
print 'p.name = ',p.name
#因为我们使用slots做了限制，所以下面绑定会失败
#p.gender = '男'
#print 'p.gender =',p.gender
