#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

top = Tk()
t = Text(top)

for i in range(10):
	t.insert(1.0,'0123456789 ')

def printText():
	print 'take a press'

bt = Button(t,text='Button',command = printText)
t.window_create('2.0',window=bt)
t.pack()
mainloop()