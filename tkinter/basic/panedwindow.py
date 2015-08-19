#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

root = Tk()

m1 = PanedWindow(root)
m1.pack(fill=BOTH, expand=1)

label1 = Label(m1, text="水平1")
m1.add(label1)

label2 = Label(m1, text="水平2")
m1.add(label2)

label3 = Label(m1, text="水平3")
m1.add(label3)

label4 = Label(m1, text="水平4")
m1.add(label4)

m3 = PanedWindow(root)
m3.pack(fill=BOTH, expand=1)

m2 = PanedWindow(m3, orient=VERTICAL)
m3.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

root.mainloop()