#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

'''
	此模块使用的是pyhdfs，源码地址：https://github.com/jingw/pyhdfs
'''

from pyhdfs import HdfsClient

def basic():
	client = HdfsClient(hosts='study:50070')
	print(client.list_status('/'))

	print '判断某个路径是否存在'
	print client.exists("/test")
	print client.exists("/data/gz/thrift-0.9.2.tar.gz")

	client = HdfsClient(hosts='study:50070')
	print client.get_file_checksum("/data/gz/bison-2.5.1.tar.gz")

	summary = client.get_content_summary("/")
	print summary

	#文件拷贝--从HDFS拷贝到本地磁盘系统
	client.copy_to_local("/data/gz/pip-7.1.2.tar.gz","/root/data/pip-7.1.2.tar.gz")
	#文件拷贝--从本地磁盘系统拷贝到HDFS系统中
	client.copy_from_local("/root/data/thrift-0.9.2.tar.gz","/data/gz/thrift-0.9.2.tar.gz")

	print client.get_home_directory()

def fileOp():
	client = HdfsClient(hosts='study:50070')