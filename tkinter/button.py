#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

master = Tk()

def callback():
	print '我被调用了'
def demo1():
	b1 = Button(master,text='我是button',command = callback)
	b2 = Button(master,text='我是button,但不能点',state=DISABLED)
	b1.pack()
	b2.pack()

def demo2():
	f = Frame(master,height=64,width=64)
	f.pack_propagate(0)
	f.pack()

	b = Button(f,text="ok",command=callback)
	b.pack(fill=BOTH,expand=1)


demo2()
mainloop()