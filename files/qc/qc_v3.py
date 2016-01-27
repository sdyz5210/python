#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import time,datetime,threading,logging
from contextlib import nested

#810632886--674867570
#多线程执行，但是执行时并没有并发效果，而是顺序执行，不确定什么原因

logging.basicConfig(filename = "qc.log",level = logging.INFO,format='[%(asctime)s %(levelname)s] %(message)s',datefmt='%Y%m%d %H:%M:%S')

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

#返回文件行数
def getLineCount():
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

class QualityControl(threading.Thread):
	def __init__(self,threadId,startLine,endLine):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.startLine = startLine
		self.endLine = endLine
	
	def run(self):
		logging.info('threadId='+str(self.threadId))
		fastqSeqR1 = FastqSeq()
		fastqSeqR2 = FastqSeq()
		fastqSeqR1List = []
		fastqSeqR2List = []
		i = 0
		with nested(open(fileInputR1,'r'),open(fileInputR2,'r')) as (r1,r2):
			while 1:
				i += 1
				a = r1.readline()
				if not a:
					break
				b = r2.readline()
				if self.startLine <= i and i <= self.endLine:
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
						(fastqSeqR1List,fastqSeqR2List) = self.toDo(fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List)
						fastqSeqR1 = FastqSeq()
						fastqSeqR2 = FastqSeq()
					if len(fastqSeqR1List) == 100000:
						self.save(fastqSeqR1List,fastqSeqR2List)
						del fastqSeqR1List[:]
						del fastqSeqR2List[:]
		self.save(fastqSeqR1List,fastqSeqR2List)

	def toDo(self,fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List):
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

	def save(self,fastqSeqR1List,fastqSeqR2List):
		with open(fileOutputR1+str(self.threadId),'a') as r1:
			for fastqSeqR1 in fastqSeqR1List:
				r1.write(fastqSeqR1.name)
				r1.write(fastqSeqR1.seq+"\n")
				r1.write(fastqSeqR1.plus)
				r1.write(fastqSeqR1.seqQ+"\n")
				r1.flush()
		with open(fileOutputR2+str(self.threadId),'a') as r2:
			for fastqSeqR2 in fastqSeqR2List:
				r2.write(fastqSeqR2.name)
				r2.write(fastqSeqR2.seq+"\n")
				r2.write(fastqSeqR2.plus)
				r2.write(fastqSeqR2.seqQ+"\n")
				r2.flush()

def main():
	linecount = getLineCount()
	global diffValue
	diffValue = judgmentValue()
	blockNum = 4
	blockSize = linecount/4
	threadList = []
	for i in range(blockNum):
		logging.info('当前线程为：'+str(i)+',执行的行数区间为：'+str(blockSize*i+1)+'--'+str(blockSize*(i+1)))
		qualityControl = QualityControl(i,blockSize*i+1,blockSize*(i+1))
		threadList.append(qualityControl)
	for t in threadList:
		t.setDaemon(True)
		t.start()
	for t in threadList:
		t.join()

if __name__ == '__main__':
	startTime = datetime.datetime.now()
	main()
	endTime = datetime.datetime.now()
	t = (endTime-startTime).total_seconds()
	logging.info('本次运行的时间---v:'+str(t))