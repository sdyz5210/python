#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from tktable import *

root = Tk()

var = ArrayVar(root)
for y in range(0, 5):
    for x in range(0, 5):
    	index = "%i,%i" % (y, x)
    	if y==0:
        	var[index] = y
        else:
        	var[index] = ""
print var.names()

table = Table(root, rows = 5,cols = 5,state='disabled',variable=var)
table.pack()

root.mainloop()