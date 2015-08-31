#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import socket
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('121.201.7.200',10000))

def sendFile(fileName):
	sock.send("ready send")
	with open(fileName,"rb") as f:
		while True:
			data = f.read(4096)
			if not data:
				break
			sock.send(data)
		time.sleep(1)
		sock.send("EOF")

def recvFile(fileName):
	sock.send('ready recv')
	with open(fileName,'wb') as f:
		while True:
			data = sock.recv(4096)
			if data == 'EOF':
				print 'recv file success!'
				break
			f.write(data)

def confirm(s,client_command):
	s.send(client_command)
	data = s.recv(4096)
	if data == 'ready':
		return True

while True:
	client_command = raw_input(">>")
	if not client_command:
		continue

	action,fileName = client_command.split()
	if action == 'put':
		if confirm(sock,client_command):
			sendFile(fileName)
		else:
			print 'send server get error'
	elif action == 'get':
		if confirm(sock,client_command):
			recvFile(fileName)
		else:
			print 'recv server get error!'
	else:
		print 'command error'

sock.close()