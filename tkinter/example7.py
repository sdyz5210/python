#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

class App:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		
		self.button = Button(frame,text='Quit',fg='red',command=frame.quit)
		self.button.pack(side=LEFT)

		self.hi_these = Button(frame,text='hello',command=self.say_hi)
		self.hi_these.pack(side=LEFT)

	def say_hi(self):
		print 'hi there,everyone!'

root = Tk()
app = App(root)
root.mainloop()
