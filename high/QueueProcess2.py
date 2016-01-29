#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import multiprocessing,Queue,os,time
from multiprocessing import Process
from random import randint

class Producer(Process):
	def __init__(self,queue):
		multiprocessing.Process.__init__(self)
		self.queue = queue

	def run(self):
		while 1:
			self.queue.put('one product')
			print multiprocessing.current_process().name
			time.sleep(randint(1,3))

class Consumer(Process):
	def __init__(self,queue):
		multiprocessing.Process.__init__(self)
		self.queue = queue
	
	def run(self):
		while 1:
			d = self.queue.get(1)
			if d!= None:
				print multiprocessing.current_process().name
				time.sleep(randint(1,4))
				continue
			else:
				break

queue = multiprocessing.Queue(10)
if __name__ == '__main__':
	processed = []
	for i in range(3):
		processed.append(Producer(queue))
		processed.append(Consumer(queue))
	for p in processed:
		p.start()
	for p in processed:
		p.join()