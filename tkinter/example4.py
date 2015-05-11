#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

top = Tk()
t = Text(top)

for i in range(10):
	t.insert(1.0,'0123456789 ')

def enterTag(event):
	print 'Event event'

def printText():
	print 'take a press'

t.tag_config('a',foreground='blue',underline=1)
t.tag_bind('a','<Enter>',enterTag)
t.insert(2.0,'Enter event','a')
t.pack()
mainloop()