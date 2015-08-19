#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

top = Tk()

lb = Listbox(top)

lb.insert(1,"python")
lb.insert(2,"Java")
lb.insert(3,"C")
lb.insert(4,"C++")
lb.insert(5,"perl")
lb.insert(6,"go")
lb.pack()

top.mainloop()