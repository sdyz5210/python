#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()
root.title('my test')

def button1():
	listbox.insert(END,'Button1 pressed')

def button2():
	text_contents = text.get()
	listbox.insert(END,text_contents)
	text.delete(0,END)

button1 = Button(root,text="button1",command=button1)
button2 = Button(root,text="button2",command=button2)
button3 = Button(root,text="button3")

text = Entry(root)
scrollbar = Scrollbar(root,orient=VERTICAL)
listbox = Listbox(root,yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)

listbox.pack()
scrollbar.pack()
mainloop()