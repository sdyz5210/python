#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#此例子运行失败，错误没有查出来呢

from Tkinter import *

#改变文字大小的，当进度条改变时
def resize(ev=None):
	label.config(font='Helvetica -%d bold ' % scale.get())

root = Tk()
root.geometry('600x400')
label = Label(root,text='very good!',fg='blue',font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)
Scale(root,from =10,to=40,orient=HORIZONTAL,command=resize).get(12).pack(fill=X,expand=1)
quit = Button(root,text='QUIT',command=root.quit , activeforeground='while',activebackground='red')

quit.pack()
mainloop()