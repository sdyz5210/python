#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import commands,datetime

startTime = datetime.datetime.now()

a,b = commands.getstatusoutput('cat R1.out.fastq0 R1.out.fastq1 R1.out.fastq2 R1.out.fastq3 >> R1.out.fastq')

endTime = datetime.datetime.now()
t = (endTime-startTime).total_seconds()
print '本次运行的时间---v:'+str(t)
print a
print b