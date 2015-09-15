#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import gzip,shutil,os

def gzipCompress(fileName):
	#生成压缩后的文件名
	tarFileName = fileName+".gz"
	with gzip.open(tarFileName, 'wb') as f_out,open(fileName,'rb') as f_in:
		shutil.copyfileobj(f_in, f_out)

def gzipUnCompress(tarFileName):
	fileName = os.path.splitext(tarFileName)[0]
	print fileName
	with gzip.open(tarFileName, 'rb') as f_in,open(fileName,'wb') as f_out:
		shutil.copyfileobj(f_in, f_out)

#if __name__ == '__main__':
	#gzipCompress("/Users/mac/Documents/data/1.fastq")
	#gzipUnCompress("/Users/mac/Documents/data/4.fastq.gz")