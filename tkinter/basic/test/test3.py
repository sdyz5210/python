#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from tkFileDialog import *

root = Tk()
root.title("Tkinter中选择文件目录")
root.geometry("500x300")
entry = Entry(root,width=40)
entry.pack(side=TOP,anchor="nw")

def callback():
    entry.delete(0,END) #清空entry里面的内容
    #调用filedialog模块的askdirectory()函数去打开文件夹
    filepath = askopenfile() 
    if filepath:
        entry.insert(0,filepath) #将选择好的路径加入到entry里面

button = Button(root,text="Open",command=callback)
button.pack(side=TOP,anchor="nw")

root.mainloop()