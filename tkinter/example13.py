#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()

v = IntVar()

Label(root,text='choose a programming language:',justify=LEFT,padx=20).pack()

Radiobutton(root,text='python',padx=20,variable=v,value=1).pack(anchor=W)

Radiobutton(root,text='perl',padx=20,variable=v,value=2).pack(anchor=W)

mainloop()