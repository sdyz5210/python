#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from pyhdfs import HdfsClient

client = HdfsClient(hosts='study:50070')
print(client.list_status('/'))

print '判断某个路径是否存在'
print client.exists("/test")
print client.exists("/data/gz/thrift-0.9.2.tar.gz")

summary = client.get_content_summary("/")
print summary

#文件拷贝--从HDFS拷贝到本地磁盘系统
client.copy_to_local("/data/gz/pip-7.1.2.tar.gz","/root/data/pip-7.1.2.tar.gz")
#文件拷贝--从本地磁盘系统拷贝到HDFS系统中
client.copy_from_local("/root/data/thrift-0.9.2.tar.gz","/data/gz/thrift-0.9.2.tar.gz")

print client.get_home_directory()