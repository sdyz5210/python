#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue
import os ,time ,random

def write(q):
	for value in ['A','B','C']:
		print 'Put %s to queue...' % value
		q.put(value)
		q.put(value+"1")
		time.sleep(random.random())

def main():
	q = Queue()
	pw = Process(target=write,args=(q,))
	pw.start()
	while 1:
		result1 = q.get(True)
		result2 = q.get(True)
		print 'result1= ',result1,"result2=",result2
		if result1=='C':
			break
	pw.join()
	
if __name__ == '__main__':
	main()