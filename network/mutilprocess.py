#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing,time

def task(msg):
	print 'msg:',msg
	time.sleep(3)
	print 'end'

def async():
	pool = multiprocessing.Pool(processes=3)
	for i in xrange(4):
		msg = "hello %d" %(i)
		pool.apply_async(task,(msg,))
	pool.close()
	pool.join()

if __name__ == '__main__':
	async()