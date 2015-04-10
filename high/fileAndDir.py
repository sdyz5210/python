#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print 'os.name =',os.name
print 'os.uname=',os.uname()
print 'os.environ=',os.environ
print 'os.getenv(path)=',os.getenv('path')

#操作文件和目录的函数一部分在os中，一部分在os.path中

#查看当前目录的绝对路径
print '查看当前目录的绝对路径',os.path.abspath('.')

#在某个目录下面创建一个新目录
#首先先把要创建的新目录的完整路径写出来：
os.path.join('/Users/mac','test')
#然后创建一个目录
os.mkdir('/Users/mac/test')
#删除一个目录
os.rmdir('/Users/mac/test')

#注意把两个路径合成一个时，不要直接拼接字符串，而是使用join方式，这在不同操作系统都适用
#同样，拆分路径也需要使用特定函数
os.path.split('/Users/mac/file.txt')
#结果为：（'/Users/mac'，'file.txt'）
#获取文件扩展名
os.path.splitext('/Users/mac/file.txt')
#结果为：('/Users/mac/file','.txt')

#重命名
os.rename('test.txt','test.py')
#删除文件
os.remove('test.py')