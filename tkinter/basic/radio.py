#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

def sel():
	selection = "You selected the optiopn "+str(var.get())
	label.config(text=selection)

top = Tk()

var = IntVar()

r1 = Radiobutton(top,text="java",variable=var, value=1,command=sel)
r1.pack( anchor = W )

r2 = Radiobutton(top,text="perl",variable=var, value=3,command=sel)
r2.pack( anchor = W )

r3 = Radiobutton(top,text="python",variable=var, value=2,command=sel)
r3.pack( anchor = W )

label = Label(top)
label.pack()

top.mainloop()