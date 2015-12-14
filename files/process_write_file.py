#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

from multiprocessing import Process
import time

'''
	小例子进行多线程对文件操作传递文件句柄或多进程中生成文件句柄时的区别。
'''

def task(name,f):
	f.write('hello')
	f.flush()

def task_demo(name):
	f = open('text.txt','a+')
	f.write('hello')

if __name__ == '__main__':
	f = open('text.txt','aw')
	#p = Process(target=task, args=('bob',f,))
	p = Process(target=task_demo, args=('bob',))
	p.start()
	p.join()