#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

import sys,os

if len(sys.argv) != 3:
	print 'Usage: *.py inputFile outputFile'
	sys.exit(0)
inputFile = sys.argv[1]
outputFile = sys.argv[2]

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
			 		my_seq = Seq(content, IUPAC.unambiguous_dna)
			 		my_seq.complement()
			 		temp = my_seq.reverse_complement()
			 		writeFile(str(temp),outputFile)
			 		content = ''
			 	writeFile(line,outputFile)
			else:
			 	content =content + line
			line = f.readline()
		if len(content) > 0:
	 		my_seq = Seq(content, IUPAC.unambiguous_dna)
			my_seq.complement()
			temp = my_seq.reverse_complement()
	 		writeFile(str(temp),outputFile)
	 		content = ''
else:
	print '您输入的不是一个文件'