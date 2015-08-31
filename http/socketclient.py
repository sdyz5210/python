#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import socket             

def example1():
	s = socket.socket()        
	host = socket.gethostname()
	port = 10000
	s.connect((host, port))
	print s.recv(1024)
	s.close

def example2():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(('localhost',10000))
	data = '10'
	sock.send(data)
	receivedData = sock.recv(1024)
	print receivedData
	sock.close()

import time
import struct
import os

def example3():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(('121.201.7.200',10000))
	sock.settimeout(1)
	while True:
		filename = raw_input('input your filename------->')#输入文件名
		fhead = struct.pack('128s11i',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)#按照规则进行打包
		sock.send(fhead)#发送文件基本信息数据
		with open(filename,"rb") as f:
			while True:        #发送文件
				filedata = f.read(1024)
				if not filedata:
					break
				sock.send(filedata)
			print "sending over..."
		sock.close()

if __name__ == '__main__':
	example3()