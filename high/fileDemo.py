#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	f = open('../README.md','r')
	print f.read()

except Exception, e:
	raise e
finally:
	if f:
		f.close()

#上面经常写会比较麻烦，python引入了with帮助处理
print '-----------------gege--------------'
with open('../README.md','r') as f1:
	print f1.read()

#read()方法会一次性读取文件内容，如果文件太大内存就爆了，为了安全起见我们可以使用其他方式 ，适应于小文件
#read(size)每次读取特定大小，适用于未知大小的文件或者大文件
#readline()每次读取一行
#readlines()一次读取所有并返回一个list，适用于配置文件

print '-----------------gege--------------'
import codecs
with codecs.open('../README.md','rb','utf-8') as ff:
	print ff.read()

#文件写和文件读对应 file。write('hello')