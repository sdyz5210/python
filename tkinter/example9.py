#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()

def hello():
	print 'hello menu'

menubar = Menu(root)

filemenu = Menu(menubar,tearoff=0)

for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_command(label = item,command = hello)

menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar

root.mainloop()