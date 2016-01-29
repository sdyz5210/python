#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from multiprocessing import Process
import time
import random
from Queue import Queue

queue = Queue(10)

class ProducerThread(Process):
	def run(self):
		nums = range(5)
		global queue
		while 1:
			if nums:
				num = random.choice(nums)
				nums.remove(num)
				print nums
				queue.put(num)
				print 'Produced',num
				time.sleep(random.random())

class ConsumerThread(Process):
	def run(self):
		global queue
		while 1:
			num = queue.get()
			queue.task_done()
			print 'Consumed',num
			time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()