#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024


ADDR = (HOST,PORT)
udpCliSock = socket(AF_INET,SOCK_DGRAM)

while 1:
	data = raw_input('>')
	if not data:
		break
	udpCliSock.sendto(data,ADDR)
	data,ADDR = udpCliSock.recvfrom(BUFSIZE)
	if not data:
		break
	print data

udpCliSock.close()