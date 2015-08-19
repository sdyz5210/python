#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import tkMessageBox

top = Tk()
label = Label(top,text="username")
label.pack(side=LEFT)

#和输入的人名sayhi
def sayHi():
	tkMessageBox.showinfo("sayHi",username.get())

username = StringVar()
entry = Entry(top,bd=5,textvariable=username,highlightcolor='blue')
entry.pack(side=RIGHT)

button = Button(top,text="show",command=sayHi)
button.pack(side=LEFT)

top.mainloop()