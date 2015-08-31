#!/usr/bin/python
# -*- coding: utf-8 -*-

import time,threading

exitFlag = 0

class ThreadDemo(threading.Thread):
	def __init__(self,threadId,name,counter):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.counter = counter
	
	def run(self):
		print "starting"+self.name
		print_time(self.name,self.counter,5)
		print "exitiong"+self.name

def print_time(threadName,delay,counter):
	while counter:
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print "%s: %s" % (threadName, time.ctime(time.time()))
		counter -= 1

thread1 = ThreadDemo(1,"thread-1",1)
thread2 = ThreadDemo(2,"thread-2",2)

thread1.start()
thread2.start()
print "Exiting Main Thread"