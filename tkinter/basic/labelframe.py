#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

root = Tk()

lf = LabelFrame(root,text="This is a LabelFrame")
lf.pack(fill="both", expand="yes")

left = Label(lf, text="Inside the LabelFrame")
left.pack()

root.mainloop()