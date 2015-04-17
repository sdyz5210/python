#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os

if len(sys.argv) != 3:
	print 'Usage: *.py inputFile outputFile'
	sys.exit(0)
inputFile = sys.argv[1]
if os.path.isfile(inputFile):
	with open(inputFile,'r') as f:
		content = ''
		line = f.readline()
		while line:
			if line.startswith('>'):
			 	writeFile(line,outputFile)
			 	line = f.readline()
			 	continue
			content +=line
			line = f.readline()
else:
	print '您输入的不是一个文件'

def writeFile(text,file):
	with open(outputFile,'w') as f:
		f.write(text)