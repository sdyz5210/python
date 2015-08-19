#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import tkMessageBox

top = Tk()

def hello():
	tkMessageBox.showinfo("hello python","hello python")

button = Button(top,text='少壮不努力,老大学编程',command=hello)

button.pack()
top.mainloop()