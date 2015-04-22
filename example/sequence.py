#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os

if len(sys.argv) != 5:
	print 'Usage: *.py scafFile contigFile gapFile seqLen'
	sys.exit(0)
scafFile = sys.argv[1]
contigFile = sys.argv[2]
gapFile = sys.argv[3]
seqLen = int(sys.argv[4])

if os.path.isfile(scafFile) and os.path.isfile(contigFile) and os.path.isfile(gapFile):
	with open('scafFile','r') as sf:
		
else:
	print '您输入的文件参数不对'