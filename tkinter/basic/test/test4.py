#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from tkFileDialog import *
from Tkinter import *
from ttk import *

root = Tk()
root.title('test')

nb = Notebook(root)
nb.pack(fill='both', expand='yes')

f1 = Text(root)
f2 = Text(root)
f3 = Text(root)

nb.add(f1, text='page1')
nb.add(f2, text='page2')
nb.add(f3, text='page3')

root.mainloop()