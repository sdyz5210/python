#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image,ImageTk
import time
master = Tk()

def demo1():
	w = Label(master,text="Hello World!")
	w.pack()

def demo2():
	w = Label(master,text="Hello World",fg="green")
	w.pack()

def demo3():
	longtext = """这是显示的是多行文字
	你能想象的到有多长吗?
	我们来猜猜看
	"""
	w = Label(master,text=longtext,anchor=W,justify=LEFT)
	w.pack()

def demo4():
	v = StringVar()
	w = Label(master,textvariable=v).pack()
	for i in range(11):
		time.sleep(1)
		v.set('Hello------'+str(i))

def demo5():
	photo = PhotoImage(file="1.gif")
	w = Label(master,image=photo)
	#搞了半天的图片问题，Mac系统一直没有显示，原来少了下面的一行代码
	w.img = photo
	w.pack()

def demo6():
	image = Image.open("3.jpeg")
	photo = ImageTk.PhotoImage(image)
	label = Label(image=photo)
	label.image = photo
	label.pack()

demo6()

mainloop()