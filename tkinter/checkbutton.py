#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()

var = IntVar()

c = Checkbutton(root,text="我是帅哥",variable=var)
c.pack()

mainloop()