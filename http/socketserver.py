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

example3()

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
