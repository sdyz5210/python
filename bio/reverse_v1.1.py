#!/usr/bin/env python
# -*- coding: utf-8 -*-

#version 1.1 此版本使用pyfasta实现。
import sys,os
from pyfasta import Fasta

if len(sys.argv) != 3:
	print 'Usage: *.py inputFile outputFile'
	sys.exit(0)
inputFile = sys.argv[1]
outputFile = sys.argv[2]

def writeFile(text,files):
	with open(files,'a') as f:
		f.write(text)

if os.path.isfile(inputFile):
	f = Fasta(inputFile)
	for key in f.keys():
		writeFile(">"+key+os.linesep,outputFile)
		content = f.sequence({'chr':key,'start':0,'stop':len(f[key])-1,'strand':'-'},one_based=False)
		writeFile(content+os.linesep,outputFile)
else:
	print '您输入的不是一个文件'