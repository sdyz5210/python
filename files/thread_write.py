#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

import threading,sys,fcntl

def writeWarnLog(file):
	fcntl.flock(file.fileno(), fcntl.LOCK_EX)
	count=0;  
	while count<100:
		file.write('2012-11-28 22:51:01|zookeeper|WARN|m1|172.17.1.15\n')  
		count+=1  
	print 'write warn log finished'
	fcntl.flock(file, fcntl.LOCK_SH)

def writeErrorLog(file):
	fcntl.flock(file.fileno(), fcntl.LOCK_EX)
	count=0;  
	while count<100:
		file.write('2012-12-12 22:22:22|zookeeper\n')  
		count+=1  
	print 'write error log finished'
	fcntl.flock(file, fcntl.LOCK_SH)

def main():  
	fileName='zookeeper.log'  
	mode='w+'           
	try:     
		f=open(fileName,mode)  
		t1=threading.Thread(target=writeWarnLog,args=(f,))  
		t2=threading.Thread(target=writeErrorLog,args=(f,))  

		t1.start()  
		t2.start()  

		t1.join()  
		t2.join()  
	except Exception,e:  
		print 'write log failed,',str(e)  
	finally:  
		f.close()
	f.close()
	print 'write log finished'  

if __name__=='__main__':  
	main()  