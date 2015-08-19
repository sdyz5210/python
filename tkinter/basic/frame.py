#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

top = Tk()

frame1 = Frame(top)
frame1.pack(side=TOP)

frame2 = Frame(top)
frame2.pack(side=BOTTOM)

button1 = Button(frame1,text="red",fg="red")
button1.pack(side=LEFT)

button2 = Button(frame1,text="blue",fg="blue")
button2.pack(side=LEFT)

button3 = Button(frame1,text="yellow",fg="yellow")
button3.pack(side=LEFT)

button4 = Button(frame2,text="green",fg="green")
button4.pack(side=BOTTOM)

top.mainloop()