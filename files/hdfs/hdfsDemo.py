#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

'''
	此例子使用的是hdfs模块
'''

from hdfs.client import Client

myClient = Client("http://study:50070") 
myClient.content("/data/gz")
hdfsPath = "/data/gz/hadoop-2.7.1.tar.gz"
localPath = "/root/data/"
#从hdfs中取出数据存放到本地系统硬盘上
myClient.download(hdfsPath,localPath)

'''
此部分代码没有走通
fq = "/data/fq/20150923.fasta"
f = myClient.read(fq)
for line in f:
	print line
'''