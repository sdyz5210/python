#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import tkMessageBox

def sayHi():
	tkMessageBox.showinfo("sayhi","hi python")

root = Tk()
button = Button(root,text="sayHi",command=sayHi)
button.pack()

root.mainloop()