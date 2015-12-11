#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
import os ,time ,random

class Demo:
	name = ""
	value = ""

class ProcessQueueDemo(multiprocessing.Process):
	def __init__(self,task_queue):
		multiprocessing.Process.__init__(self)
		self.task_queue = task_queue

	def run(self):
		for i in ['A','B','C']:
			print 'Put %s to queue...' % i
			d = Demo()
			d.name = i
			d.value = i+'1'
			self.task_queue.put(d)
			time.sleep(random.random())

if __name__ == '__main__':
	task_queue = multiprocessing.Queue()
	pqd = ProcessQueueDemo(task_queue)
	pqd.start()
	while 1:
		d = task_queue.get(True)
		print 'result1= ',d.name,"result2=",d.value
		if d.name == 'C':
			break
	pqd.join()