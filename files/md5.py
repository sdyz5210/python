#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

#计算文件的MD5值

import hashlib
import os,sys

#计算字符串的md5
def GetStrMd5(src):
    m = hashlib.md5()
    m.update(src)
    print m.hexdigest()

#计算文件的MD5
def getFileMD5(filePath):
    m = hashlib.md5()
    with open(filePath,"rb") as f:
        m.update(f.read())
    return m.hexdigest()
#计算大文件的MD5
def getBigFileMD5(filePath):
	m = hashlib.md5()
	with open(filePath,"rb") as f:
		while True:
			data = f.read(8096)
			if not data:
				break
			m.update(data)
	return m.hexdigest()

#计算文件的SHA1
def getFileSHA1(filePath):
    s = hashlib.sha1()
    with open(filePath,"rb") as f:
        s.update(f.read())
    return s.hexdigest()

def main():
	#print getFileMD5("testExcel.py")
	#print getFileSHA1("testExcel.py")
	print getBigFileMD5("/Users/mac/Documents/data/1.fastq.gz")

if __name__ == '__main__':
	main()