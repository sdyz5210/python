#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple,deque

#namedtuple的用法为：namedtuple('名称',[属性list])
#使用namedtuple表示一个点的坐标
Point = namedtuple('point',['x','y'])
p = Point(3,5)
print '打印点得x坐标',p.x
print '打印点得y坐标',p.y

#使用namedtuple表示一个圆
Circle = namedtuple('circle',['x','y','r'])


#使用deque双向链表

q = deque(['a','b','c','d'])
print q
q.append('e')
print '打印列表追加后的结果',q
q.appendleft('c')
print '打印列表在左侧增加的结果',q

#使用dict时，如果希望key值不存在时，返回一个默认值，就可以使用defaultdict

#……OrderedDict
#……Counter