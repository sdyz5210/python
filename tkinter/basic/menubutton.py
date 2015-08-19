#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

top = Tk()
mb = Menubutton(top,text="课程",relief=RAISED)
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
mayoVar  = IntVar()
ketchVar = IntVar()

def donothing():
	print 'sb,donothing'

mb.menu.add_checkbutton (label="java",variable=mayoVar,command=donothing)
mb.menu.add_checkbutton (label="python",variable=ketchVar,command=donothing)
mb.pack()
top.mainloop()