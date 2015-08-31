#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import socket

def example1():
	s = socket.socket()
	host = socket.gethostname()
	port = 10000
	s.bind((host,port))
	s.listen(5)
	while True:
		c,addr = s.accept()
		print 'got connection from',addr
		c.send('thank you for connection')
		c.close()

def example2():
	#第一个参数：地址族 一般都是AF_INET
	#第二个参数：指定连接方式SOCK_STREAM->TCP,SOCK_DGRAM->UDP
	#第三个参数：定义使用的协议
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('localhost',10000))
	sock.listen(1)
	while True:
		print 'waiting for connecting...'
		connection,address = sock.accept()
		print '...connected from:%s:%i'%(address[0],address[1])
		while True:
			data = connection.recv(1024)
			if not data:
				break
			result = 0
			for i in range(1,int(data)+1):
				result = result+reduce(lambda x,y:x*y,range(1,i+1))
			connection.send('the result is %i'%result)
		connection.close
	sock.close

#分叉
#每当有客户端请求时，就创建一个子进程,由子进程处理客户端请求，父进程监听；缺点就是比较耗费资源
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class ForkServer(ForkingMixIn, TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handle(self):
		while True:
			data = self.request.recv(1024)
			if not data:
				break
			result = 0
			for i in range(1,int(data)+1):
				result = result+reduce(lambda x,y:x*y,range(1,i+1))
			self.request.send('the result is %i'%result)

def example3():
	server = ForkServer(('localhost', 10000), Handler)
	server.serve_forever()

#多线程
#资源消费比较少，但是存在共享资源同步问题
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

class ThreadServer(ThreadingMixIn, TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handle(self):
		while True:
			data = self.request.recv(1024)
			if not data:
				break
			result = 0
			for i in range(1,int(data)+1):
				result = result+reduce(lambda x,y:x*y,range(1,i+1))
			self.request.send('the result is %i'%result)

def example4():
	server = ThreadServer(('localhost', 10000), Handler)
	server.serve_forever()

import threading
import time
import struct

class UploadHandler(StreamRequestHandler):
	def handle(self):
		FILEINFO_SIZE = struct.calcsize('128s32sI8s')
		while True:
			fhead = self.request.recv(FILEINFO_SIZE)
			filename,temp1,filesize,temp2 = struct.unpack('128s32sI8s',fhead)
			print filename,len(filename),type(filename)
			print filesize
			#命名新文件new_传送的文件
			filename = "new_"+filename.strip('\00')
			with open(filename,'wb') as f:
				restsize = filesize
				print "recving..."
				while True:
					#如果剩余数据包大于1024，就去1024的数据包
					if restsize < 1024:
						filedata = self.request.recv(restsize)
					else:
						filedata = self.request.recv(1024)
					if not filedata:
						break
					f.write(filedata)
					restsize = restsize - len(filedata)#计算剩余数据包大小
					if restsize <= 0:
						break

def example5_2():
	server = ThreadServer(('192.168.100.123', 10000), UploadHandler)
	server.serve_forever()

if __name__ == '__main__':
	example5_2()