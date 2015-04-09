#!/usr/bin/python
# -*- coding: utf-8 -*-

#dict和其他语言的map很类似

map = {"Tom":87,"Jack":95,"John":75}
print '打印dict map=',map
print '打印Jack的成绩:',map['Jack']

print '--------删除dict中的元素-------'
map.pop('John')
print '打印dict map=',map

print '--------判断是否存在某元素------'
print 'map中是否存在Tom:','Tom' in map
print 'map中是否存在merry:','merry' in map
print 'map中是否存在Tom:', map.get('Tom')
print 'map中是否存在merry:', map.get('merry',-1)