#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

top = Tk()

text = Text(top)
text.insert(INSERT,"hello python")
text.insert(END,"BYE,END")
text.pack()

text.tag_add("here","1.0","1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
top.mainloop()