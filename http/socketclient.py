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

example2()