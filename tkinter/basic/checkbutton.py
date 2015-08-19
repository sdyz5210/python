#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import tkMessageBox

top = Tk()

#显示选中与否的值
def show():
	print cv1.get()

cv1 = IntVar()
cv2 = IntVar()
cb1 = Checkbutton(top,text = "Music", variable = cv1, onvalue = 1, offvalue = 0, height=5, width = 20,command=show)
cb2 = Checkbutton(top,text = "Music", variable = cv2, onvalue = 1, offvalue = 0, height=5, width = 20,command=show)
cb1.pack()
cb2.pack()
top.mainloop()