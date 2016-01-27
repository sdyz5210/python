#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import time,datetime
from itertools import izip
from contextlib import nested

fileInputR1 = 'WGC037752_MISEQ_FFPE_Cptest_combined_clean_R1.fastq'
fileInputR2 = 'WGC037752_MISEQ_FFPE_Cptest_combined_clean_R2.fastq'
fileOutputR1 = 'R1.out.fastq'
fileOutputR2 = 'R2.out.fastq'
defaultQcValue = 20
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
	r1Position = 0
	r2Position = 0
	r1_q_isok = False
	r2_q_isok = False
	for i,c in enumerate(fastqSeqR1.seqQ):
		temp = int(ord(c))-diffValue
		r1Position = i
		if temp < defaultQcValue:
			r1_q_isok = True
			break
	if not r1_q_isok:
		r1Position += 1
	if r1Position <= defaultLength:
		return (fastqSeqR1List,fastqSeqR2List)
	else:
		for i,c in enumerate(fastqSeqR2.seqQ):
			temp = int(ord(c))-diffValue
			r2Position = i
			if temp < defaultQcValue:
				r2_q_isok = True
				break
	if not r2_q_isok:
		r2Position += 1
	if r2Position <= defaultLength:
		return (fastqSeqR1List,fastqSeqR2List) 
	else:
		#质量合格的保存
		fastqSeqR1.seq = fastqSeqR1.seq[0:r1Position]
		fastqSeqR1.seqQ = fastqSeqR1.seqQ[0:r1Position]
		fastqSeqR2.seq = fastqSeqR2.seq[0:r2Position]
		fastqSeqR2.seqQ = fastqSeqR2.seqQ[0:r2Position]
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
		i = 0
		fastqSeqR1 = FastqSeq()
		fastqSeqR2 = FastqSeq()
		for a,b in izip(r1, r2):
			i += 1
			if i%4 == 1:
				fastqSeqR1.name = a
				if not fastqSeqR1.name:
					break
				fastqSeqR2.name = b
			elif i%4 == 2:
				fastqSeqR1.seq = a
				fastqSeqR2.seq = b
			elif i%4 == 3:
				fastqSeqR1.plus = a
				fastqSeqR2.plus = b
			elif i%4 == 0:
				fastqSeqR1.seqQ = a
				fastqSeqR2.seqQ = b
				(fastqSeqR1List,fastqSeqR2List) = toDo(fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List)
				fastqSeqR1 = FastqSeq()
				fastqSeqR2 = FastqSeq()
			if len(fastqSeqR1List) == 100000:
				save(fastqSeqR1List,fastqSeqR2List)
				del fastqSeqR1List[:]
				del fastqSeqR2List[:]
		save(fastqSeqR1List,fastqSeqR2List)

if __name__ == '__main__':
	startTime = datetime.datetime.now()
	main()
	endTime = datetime.datetime.now()
	t = (endTime-startTime).total_seconds()
	print '本次运行的时间---v2:',t