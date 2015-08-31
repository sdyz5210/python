#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import tktable

root = Tk()
root.title("Probabilidade e estatistica")

table = tktable.Table(root, rows=2, cols=10)
table.pack()

root.mainloop()