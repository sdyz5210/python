#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import linecache

fileInputR1 = '/Users/mac/Documents/data/fastq/R1.fastq'
fileInputR2 = '/Users/mac/Documents/data/fastq/R2.fastq'
defaultValue = 20
fileOutputR1 = '/Users/mac/Documents/data/fastq/R1.out.fastq'
fileOutputR2 = '/Users/mac/Documents/data/fastq/R2.out.fastq'
defaultLength = 30
global diffValue
diffValue = 0

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

def save(fastqSeqR1,fastqSeqR2):
	print 'todo'
	with open(fileOutputR1,'a') as r1:
		r1.write(fastqSeqR1.name)
		r1.write(fastqSeqR1.seq)
		r1.write(fastqSeqR1.plus)
		r1.write(fastqSeqR1.seqQ)
		r1.flush()

	with open(fileOutputR2,'a') as r2:
		r2.write(fastqSeqR2.name)
		r2.write(fastqSeqR2.seq)
		r2.write(fastqSeqR2.plus)
		r2.write(fastqSeqR2.seqQ)
		r2.flush()

def toDo(fastqSeqR1,fastqSeqR2):
	r1_q_isok = False
	r2_q_isok = False
	r1Length = r2Length =0
	for i,c in enumerate(fastqSeqR1.seqQ):
		temp = int(ord(c))-diffValue
		if temp < defaultValue:
			if i-1 >= defaultLength:
				print 'r1',temp,defaultValue
				fastqSeqR1.seq = fastqSeqR1.seq[0:i-1]
				fastqSeqR1.seqQ = fastqSeqR1.seqQ[0:i-1]
				r1_q_isok = True
				r1Length = i-1
			break
	if not r1_q_isok:
		return
	else:
		for i,c in enumerate(fastqSeqR2.seqQ):
			temp = int(ord(c))-diffValue
			if temp < defaultValue:
				if i-1 >= defaultLength:
					print 'r1',temp,defaultValue
					fastqSeqR2.seq = fastqSeqR2.seq[0:i-1]
					fastqSeqR2.seqQ = fastqSeqR2.seqQ[0:i-1]
					r2_q_isok = True
					r2Length = i-1
				break
	if not r2_q_isok:
		return 
	else:
		if r1Length > r2Length:
			fastqSeqR1.seq = fastqSeqR1.seq[0:r2Length]
			fastqSeqR1.seqQ = fastqSeqR1.seqQ[0:r2Length]
		else:
			fastqSeqR2.seq = fastqSeqR2.seq[0:r1Length]
			fastqSeqR2.seqQ = fastqSeqR2.seqQ[0:r1Length]
		#质量合格的保存
		save(fastqSeqR1,fastqSeqR2)

def judgmentValue(linecount):
	diffValue = 0
	j = 0
	with open(fileInputR1,'r') as r1:
		j += 1
		line = r1.readline()

	for i in range(4,linecount,4):
		seqQ = linecache.getline(fileInputR1,i)
		for j,c in enumerate(seqQ):
			temp = int(ord(c))
			if temp < 59:
				diffValue = 33
				break
			if temp > 74:
				diffValue = 64
				break
		if diffValue!=0:
			break
def main():
	judgmentValue(linecount)
	with nested(open(fileInputR1,'r'),open(fileInputR2,'r')) as (r1,r2):


if __name__ == '__main__':
	main()
