#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
fasta格式数据截取操作，根据输入的文件内容和制定的截取文件大小
把截取的结果输出到指定文件中
start:开始位置
end:结束位置
os.linesep:根据不同操作系统获取不同的换行符
'''

import sys,os

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

if os.path.isfile(inputFile):
	with open(inputFile,'r') as f:
		content = ''
		line = f.readline()
		while line:
			if line.startswith('>'):
			 	if len(content) > 0:
			 		content = content[start-1:end-1]+os.linesep
			 		writeFile(content,outputFile)
			 		content = ''
			 	writeFile(line,outputFile)
			else:
			 	content =content + line
			line = f.readline()
		if len(content) > 0:
	 		content = content[start-1:end-1]+os.linesep
	 		writeFile(content,outputFile)
	 		content = ''
else:
	print '您输入的不是一个文件'
