#!/usr/bin/python
# -*- coding: utf-8 -*-

import time,thread

def print_time(threadName,delay):
	count = 0
	while count<5:
		time.sleep(delay)
		count+=1
		print "%s:%s" %(threadName,time.ctime(time.time()))

try:
	thread.start_new_thread(print_time,("thread-1",2,))
	thread.start_new_thread(print_time,("thread-2",4,))
except Exception, e:
	raise e

while 1:
	pass