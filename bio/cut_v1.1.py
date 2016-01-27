#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
fasta格式数据截取操作，根据输入的文件内容和制定的截取文件大小
把截取的结果输出到指定文件中
start:开始位置
end:结束位置
os.linesep:根据不同操作系统获取不同的换行符
'''
#version 1.1
#此版本使用pyfasta进行实现
import sys,os
from pyfasta import Fasta

if len(sys.argv) != 5:
	print 'Usage: *.py inputFile outputFile start end'
	sys.exit(0)
inputFile = sys.argv[1]
outputFile = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])

def writeFile(text,files):
	with open(files,'a') as f:
		f.write(text)

f = Fasta(inputFile)
for key in f.keys():
	writeFile(">"+key+os.linesep,outputFile)
	writeFile(f[key][start:end]+os.linesep,outputFile)
