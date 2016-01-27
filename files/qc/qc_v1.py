#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import time,datetime
from itertools import izip
from contextlib import nested

#fileInputR1 = '/Users/mac/Documents/data/fastq/R1.fastq'
#fileInputR2 = '/Users/mac/Documents/data/fastq/R2.fastq'
#fileOutputR1 = '/Users/mac/Documents/data/fastq/R1.out.fastq'
#fileOutputR2 = '/Users/mac/Documents/data/fastq/R2.out.fastq'
fileInputR1 = 'R1.fastq'
fileInputR2 = 'R2.fastq'
fileOutputR1 = 'R1.out.fastq'
fileOutputR2 = 'R2.out.fastq'
defaultValue = 20
defaultLength = 30

class FastqSeq():
	name = ''
	seq = ''
	plus = ''
	seqQ = ''

def getLineCount(type):
	if type == 0:
		#linecount = 29905408
		linecount = -1
		for linecount, line in enumerate(open(fileInputR1, 'rU')):
			pass
		linecount += 1
		return linecount
	elif type == 1:
		with open(fileInputR1,'r') as r1:
			linecount=len(r1.readlines())
			return linecount
	else:
		with open(fileInputR1,'r') as r1:
			return sum(1 for x in r1)

def save(fastqSeqR1List,fastqSeqR2List):
	with open(fileOutputR1,'a') as r1:
		for fastqSeqR1 in fastqSeqR1List:
			r1.write(fastqSeqR1.name)
			r1.write(fastqSeqR1.seq+"\n")
			r1.write(fastqSeqR1.plus)
			r1.write(fastqSeqR1.seqQ+"\n")
			r1.flush()

	with open(fileOutputR2,'a') as r2:
		for fastqSeqR2 in fastqSeqR2List:
			r2.write(fastqSeqR2.name)
			r2.write(fastqSeqR2.seq+"\n")
			r2.write(fastqSeqR2.plus)
			r2.write(fastqSeqR2.seqQ+"\n")
			r2.flush()

def toDo(fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List):
	r1_q_isok = False
	r2_q_isok = False
	r1Length = r2Length = 0
	for i,c in enumerate(fastqSeqR1.seqQ):
		temp = int(ord(c))-diffValue
		if temp < defaultValue:
			if i-1 >= defaultLength:
				fastqSeqR1.seq = fastqSeqR1.seq[0:i-1]
				fastqSeqR1.seqQ = fastqSeqR1.seqQ[0:i-1]
				r1_q_isok = True
				r1Length = i-1
			break
	if not r1_q_isok:
		return (fastqSeqR1List,fastqSeqR2List)
	else:
		for i,c in enumerate(fastqSeqR2.seqQ):
			temp = int(ord(c))-diffValue
			if temp < defaultValue:
				if i-1 >= defaultLength:
					fastqSeqR2.seq = fastqSeqR2.seq[0:i-1]
					fastqSeqR2.seqQ = fastqSeqR2.seqQ[0:i-1]
					r2_q_isok = True
					r2Length = i-1
				break
	if not r2_q_isok:
		return (fastqSeqR1List,fastqSeqR2List) 
	else:
		#质量合格的保存
		fastqSeqR1List.append(fastqSeqR1)
		fastqSeqR2List.append(fastqSeqR2)
		return (fastqSeqR1List,fastqSeqR2List)

def judgmentValue():
	diffValue = 0
	j = 0
	with open(fileInputR1,'r') as r1:
		while 1:
			j += 1
			line = r1.readline()
			if j%4 == 0:
				for j,c in enumerate(line):
					temp = int(ord(c))
					if temp < 59:
						diffValue = 33
						break
					if temp > 74:
						diffValue = 64
						break
			if diffValue!=0:
				break
		return diffValue
		
def main():
	global diffValue
	diffValue = judgmentValue()
	fastqSeqR1List = []
	fastqSeqR2List = []
	with nested(open(fileInputR1,'r'),open(fileInputR2,'r')) as (r1,r2):
		while 1:
			fastqSeqR1 = FastqSeq()
			fastqSeqR1.name = r1.readline()
			if not fastqSeqR1.name:
				break
			fastqSeqR1.seq = r1.readline()
			fastqSeqR1.plus = r1.readline()
			fastqSeqR1.seqQ = r1.readline()
			fastqSeqR2 = FastqSeq()
			fastqSeqR2.name = r2.readline()
			fastqSeqR2.seq = r2.readline()
			fastqSeqR2.plus = r2.readline()
			fastqSeqR2.seqQ = r2.readline()
			(fastqSeqR1List,fastqSeqR2List) = toDo(fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List)
			if len(fastqSeqR1List) == 50000:
				save(fastqSeqR1List,fastqSeqR2List)
				del fastqSeqR1List[:]
				del fastqSeqR2List[:]
		save(fastqSeqR1List,fastqSeqR2List)

if __name__ == '__main__':
	startTime = datetime.datetime.now()
	main()
	endTime = datetime.datetime.now()
	t = (endTime-startTime).total_seconds()
	print '本次运行的时间---v1:',t