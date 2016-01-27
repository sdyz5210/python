#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while 1:
	print 'warting for message...'
	data,addr = udpSerSock.recvfrom(BUFSIZE)
	udpSerSock.sendto('[%s] %s'%(ctime(),data),addr)
	print '...received from and retuned to:',addr

udpSerSock.close()