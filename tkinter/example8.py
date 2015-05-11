#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

def func(value):
	if value.get() == 'kikc':
		value.set('prada')
	else:
		value.set('kikc')

win = Frame(None,width=200,height=200)
win.pack_propagate(0)
win.pack()

value=StringVar()

widget = Button(win,textvariable=value,command=(lambda:func(value)))
widget.pack()
value.set('nba')

win.mainloop()