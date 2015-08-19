#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import Tkinter as tk
 
class MyWindow():
    def __init__(self):
        self.root = tk.Tk()
        button=tk.Button(self.root, text='NEXT',
                         command=self.OnNext)
        button.pack()
         
    def OnNext(self):
        win = MyWindow()
        self.root.destroy()
         
win = MyWindow()
win.root.mainloop()