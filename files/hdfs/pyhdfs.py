#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from snakebite.client import Client
import glob

'''
使用snakebite可以读取hdfs中数据的信息
目前没有发现往HDFS中写入数据的方法
'''

def display():
	client = Client("study", 9000, use_trash=False)
	for x in client.ls(['/data/gz']):
		print x

def copy():
	client = Client("study", 9000, use_trash=False)
	client.copyToLocal(["/data/gz"],"/root/data/",check_crc=False)

def count():
	client = Client("study", 9000, use_trash=False)
	count = client.count(["/data/gz"])
	for i in count:
		print i

def getDf():
	client = Client("study", 9000, use_trash=False)
	info = client.df()
	print info

def delete():
	client = Client("study", 9000, use_trash=False)
	client.delete(["/data/gz"], recurse=False)

def test():
	for filename in glob.glob("/Users/mac/Documents/data/fastq/*.fastq"):
		print filename

if __name__ == '__main__':
	copy()
