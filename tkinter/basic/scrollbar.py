#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
root = Tk()

sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

lb = Listbox(root,yscrollcommand=sb.set)

for i in range(10):
	lb.insert(END,str(i))

lb.pack(side=LEFT,fill=BOTH)
sb.config(command=lb.yview)
mainloop()