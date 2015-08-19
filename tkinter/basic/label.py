#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import math
import tkMessageBox

#A label and a button

def labelAndButton():
	import sys,Tkinter
	Tkinter.Label(text="Welcome!").pack()
	Tkinter.Button(text="Exit",command=sys.exit).pack()
	Tkinter.mainloop()

#Basic coding styles with labels

def labelStyles():
	label = Label(None,text="Hello GUI world!")
	label.pack()
	label.mainloop()

def labelSide():
	root = Tk()
	Label(root,text="Hello GUI world!").pack(side=TOP)
	root.mainloop()

def labelFrame():
	root = Tk()
	root.title("Labeler")
	root.geometry("200x500")
	app = Frame(root)
	app.grid()

	label = Label(app,text="I am a label!")
	label.grid()
	root.mainloop()

def labelText():
	root = Tk()
	top = Frame(root)
	top.pack(side='top')

	hwframe = Frame(top)
	hwframe.pack(side='top',anchor='w')
	font='times 18 bold'
	hwtext = Label(hwframe, text='Hello, World!', font=font)
	hwtext.pack(side='top', pady=20)

	rframe = Frame(top)
	rframe.pack(side='top', padx=10, pady=20, anchor='w')
	r_label = Label(rframe, text='The sine of')
	r_label.pack(side='left')
	r = StringVar() 
	r.set('1.2')    
	r_entry = Entry(rframe, width=6, textvariable=r)
	r_entry.pack(side='left')
	root.mainloop()

def labelWH():
	root = Tk()
	# family, size, style
	labelfont = ('times', 20, 'bold')                  
	label = Label(root, text='Hello config world')
	label.config(height=10, width=20)
	label.pack(expand=YES, fill=BOTH)
	root.mainloop()

def labelBackground():
	root = Tk()
	labelfont = ('times', 20, 'bold')                  
	label = Label(root, text='Hello config world')
	label.config(bg='black', fg='yellow')             
	label.pack(expand=YES, fill=BOTH)
	root.mainloop()

if __name__ == '__main__':
	#labelAndButton()
	#labelStyles()
	#labelSide()
	#labelFrame()
	#labelText()
	#labelWH()
	labelBackground()



























