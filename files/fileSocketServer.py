#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import socket
import time
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class ForkServer(ForkingMixIn, TCPServer):
	pass

class Handler(StreamRequestHandler):
	def recvFile(self,fileName):
		self.request.send('ready')
		with open(fileName,'wb') as f:
			while True:
				data = self.request.recv(4096)
				if data == 'EOF':
					print 'recv file success!'
					break
				f.write(data)

	def sentFile(self,fileName):
		self.request.send("ready")
		with open(fileName,"rb") as f:
			while True:
				data = f.read(4096)
				if not data:
					break
				self.request.send(data)
			time.sleep(1)
			self.request.send("EOF")

	def handle(self):
		while True:
			data = self.request.recv(4096)
			print data
			if not data:
				break
			else:
				action,fileName = data.split()
				if action == "put":
					print 'start'
					self.recvFile(fileName)
				elif action == 'get':
					self.sentFile(fileName)
				else:
					print "get error"
					continue
		

server = ForkServer(('localhost', 10000), Handler)
server.serve_forever()