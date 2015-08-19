#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import math
import tkMessageBox

root = Tk()
top = Frame(root)
top.pack(side='top')

label = Label(top,text='Hello,world!')
label.pack(side='top')

r = StringVar()
r.set('1.2')
r_entry = Entry(top,width=6,textvariable=r)
r_entry.pack(side='top')

s = StringVar()

def comp_s(event):
	global s
	s.set('%g' % math.sin(float(r.get())))

r_entry.bind('<Return>',comp_s)

compute = Label(top,text=' equals ')
compute.pack(side='top')

s_label = Label(top,textvariable=s,width=18)
s_label.pack(side='top')

root.bind('<q>',quit)
def quit(event):
	if tkMessageBox.askokcancel('Quit','Do you really want to quit?'):
		root.destroy()
root.mainloop()


