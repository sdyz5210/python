#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import time,datetime,multiprocessing,logging,psutil,commands,sys,os
from contextlib import nested

#810632886--674867570
#多进程执行
fileInputR1 = 'WGC037752_MISEQ_FFPE_Cptest_combined_clean_R1.fastq'
fileInputR2 = 'WGC037752_MISEQ_FFPE_Cptest_combined_clean_R2.fastq'
fileOutputR1 = 'R1.out.fastq'
fileOutputR2 = 'R2.out.fastq'
defaultQcValue = 20
defaultLength = 30

logging.basicConfig(filename = "qc.log",level = logging.INFO,format='[%(asctime)s %(levelname)s] %(message)s',datefmt='%Y%m%d %H:%M:%S')

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

def save(fastqSeqR1List,fastqSeqR2List,processId):
	with open(fileOutputR1+str(processId),'a') as r1:
		for fastqSeqR1 in fastqSeqR1List:
			r1.write(fastqSeqR1.name)
			r1.write(fastqSeqR1.seq+"\n")
			r1.write(fastqSeqR1.plus)
			r1.write(fastqSeqR1.seqQ+"\n")
			r1.flush()
	with open(fileOutputR2+str(processId),'a') as r2:
		for fastqSeqR2 in fastqSeqR2List:
			r2.write(fastqSeqR2.name)
			r2.write(fastqSeqR2.seq+"\n")
			r2.write(fastqSeqR2.plus)
			r2.write(fastqSeqR2.seqQ+"\n")
			r2.flush()

def toDo(fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List):
	r1Position = 0
	r2Position = 0
	for i,c in enumerate(fastqSeqR1.seqQ):
		temp = int(ord(c))-diffValue
		r1Position = i
		if temp < defaultQcValue:
			break
	if r1Position <= defaultLength:
		return (fastqSeqR1List,fastqSeqR2List)
	else:
		for i,c in enumerate(fastqSeqR2.seqQ):
			temp = int(ord(c))-diffValue
			r2Position = i
			if temp < defaultQcValue:
				break
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

def task(processId,startLine,endLine):
	logging.info('开始执行进程：'+str(processId)+'--开始行数：'+str(startLine)+'--结束行数：'+str(endLine))
	fastqSeqR1 = FastqSeq()
	fastqSeqR2 = FastqSeq()
	fastqSeqR1List = []
	fastqSeqR2List = []
	i = 1
	with nested(open(fileInputR1,'r'),open(fileInputR2,'r')) as (r1,r2):
		while 1:
			nameR1 = r1.readline()
			seqR1 = r1.readline()
			plusR1 = r1.readline()
			seqQR1 = r1.readline()
			nameR2 = r2.readline()
			seqR2 = r2.readline()
			plusR2 = r2.readline()
			seqQR2 = r2.readline()
			if not nameR1:
				break
			if startLine <= i and i <= endLine:
				fastqSeqR1.name = nameR1
				fastqSeqR1.seq = seqR1
				fastqSeqR1.plus = plusR1
				fastqSeqR1.seqQ = seqQR1
				fastqSeqR2.name = nameR2
				fastqSeqR2.seq = seqR2
				fastqSeqR2.plus = plusR2
				fastqSeqR2.seqQ = seqQR2
				(fastqSeqR1List,fastqSeqR2List) = toDo(fastqSeqR1,fastqSeqR2,fastqSeqR1List,fastqSeqR2List)
				fastqSeqR1 = FastqSeq()
				fastqSeqR2 = FastqSeq()
				if len(fastqSeqR1List) == 100000:
					save(fastqSeqR1List,fastqSeqR2List,processId)
					del fastqSeqR1List[:]
					del fastqSeqR2List[:]
			i += 4
	save(fastqSeqR1List,fastqSeqR2List,processId)

def main():
	linecount = getLineCount()
	logging.info('当前文件的总行数为：'+str(linecount))
	global diffValue
	diffValue = judgmentValue()
	blockNum = 4
	pool = multiprocessing.Pool(processes=blockNum)
	totalRecord = linecount/4
	processAverageRecord = int(totalRecord/4)
	processAverageLines = processAverageRecord * 4
	threadList = []
	for i in range(blockNum):
		if i < 3:
			pool.apply_async(task,(i,processAverageLines*i+1,processAverageLines*(i+1),))
		else:
			pool.apply_async(task,(i,processAverageLines*i+1,linecount,))
	pool.close()
	pool.join()
	logging.info('开始执行结果合并')
	catCommandR1 = 'cat '
	catCommandR2 = 'cat '
	rmCommandR1 = 'rm -rf '
	rmCommandR2 = 'rm -rf '
	for i in range(blockNum):
		catCommandR1 += fileOutputR1+str(i)
		catCommandR1 += ' '
		catCommandR2 += fileOutputR2+str(i)
		catCommandR2 += ' '
		rmCommandR1 += fileOutputR1+str(i)
		rmCommandR1 += ' '
		rmCommandR2 += fileOutputR2+str(i)
		rmCommandR2 += ' '
	catCommandR1 += '>> '+fileOutputR1
	catCommandR2 += '>> '+fileOutputR2
	commands.getstatusoutput(catCommandR1)
	commands.getstatusoutput(catCommandR2)
	commands.getstatusoutput(rmCommandR1)
	commands.getstatusoutput(rmCommandR2)
	logging.info('结果合并结束，并已删除中间结果文件')

def input():
	if len(sys.argv) != 6:
		print 'Usage: *.py R1 R2 R1out R2out defaultQcValue defaultLength'
		sys.exit(0)
	fileInputR1 = sys.argv[1]
	fileInputR2 = sys.argv[2]
	fileOutputR1 = sys.argv[3]
	fileOutputR2 = sys.argv[4]
	defaultQcValue = sys.argv[5]
	defaultLength = sys.argv[6]

if __name__ == '__main__':
	startTime = datetime.datetime.now()
	main()
	endTime = datetime.datetime.now()
	t = (endTime-startTime).total_seconds()
	logging.info('本次运行的时间---v4:'+str(t))