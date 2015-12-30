#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import datetime
from itertools import izip
from contextlib import nested

fileInputR1 = '/Users/mac/Documents/data/fastq/R1.fastq'
fileInputR2 = '/Users/mac/Documents/data/fastq/R2.fastq'
fileOutputR1 = '/Users/mac/Documents/data/fastq/R1.out.fastq'
fileOutputR2 = '/Users/mac/Documents/data/fastq/R2.out.fastq'


#read1= 29905409
#本次运行的时间 16.14015
def read1():
	with nested(open(fileInputR1,'r'),open(fileInputR2,'r')) as (r1,r2):
		i = 0
		while 1:
			i += 1
			line = r1.readline()
			if not line:
				break
		print 'read1=',i

#read2= 29905408
#本次运行的时间 6.232195
#read2= 29905408
#本次运行的时间 5.170198
def read2():
	with nested(open(fileInputR1,'r'),open(fileInputR2,'r')) as (r1,r2):
		i = 0
		for a,b in izip(r1, r2):
			i += 1
			if i == 20000000:
				print a
				print b
		print 'read2=',i

if __name__ == '__main__':
	startTime = datetime.datetime.now()
	#read2()
	for i in range(4):
		print i
	endTime = datetime.datetime.now()
	t = (endTime-startTime).total_seconds()
	print '本次运行的时间',t