#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import socket
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class ForkServer(ForkingMixIn, TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handle(self):
		filePath = "/Users/mac/Documents/data/2.fastq.gz"
		with open(filePath,"wb") as f:
			while True:
				data = self.request.recv(10240)
				if data == 'EOF':
					print "success"
					break
				f.write(data)
				f.flush()
			self.request.send('接收成功')

server = ForkServer(('localhost', 10000), Handler)
server.serve_forever()