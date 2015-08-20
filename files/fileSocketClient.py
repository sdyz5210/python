#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',10000))
filePath = "/Users/mac/Documents/data/1.fastq.gz"
with open(filePath,"rb") as f:
	while True:
		data = f.read(10240)
		if not data:
			break
		sock.send(data)
	sock.send("EOF")
receivedData = sock.recv(1024)
print receivedData
sock.close()