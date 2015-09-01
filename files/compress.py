#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import gzip,shutil

def zipCompress():
	pass

def gzipCompress():
	with gzip.open('1.gz', 'wb') as f_out,open('/Users/mac/Documents/data/1.fastq','rb') as f_in:
		shutil.copyfileobj(f_in, f_out)

gzipCompress()