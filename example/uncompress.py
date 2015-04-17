#!/usr/bin/env python
# -*- coding:utf-8 -*-
#把制定目录下所有gz压缩文件，解压缩到制定的目录下

import sys,os,tarfile

#sys.argv[0]:当前py文件的名称
#sys.argv[1]:输入的第一个参数--制定的目录
#sys.argv[2]:输入的第二个参数--加压缩的目录
if len(sys.argv) != 3:
	print 'Usage: *.py currentPath uncompressPath'
	sys.exit(0)
currentPath = sys.argv[1]
uncompressPath = sys.argv[2]
lists = []
if os.path.isdir(currentPath) && os.path.isdir(uncompressPath) :
	for root,dirs,files in os.walk(currentPath):
		for f in files:
			if f.endswith('.gz'):
				lists.append(os.path.join(root,f))
				tar = tarfile.open(os.path.join(root,f))
				tar.extractall(path=uncompressPath)
				tar.close()
else:
	print '您输入不是一个目录'