#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

root = Tk()

spinbox = Spinbox(root,from_=0,to=10)
spinbox.pack()

root.mainloop()