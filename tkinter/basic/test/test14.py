#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

master = Tk()
master.geometry('600x400+200+100')
frame = Frame(master)
frame.pack(fill=BOTH,expand=1)

#table = TableCanvas(tframe)
#table.createTableFrame()

data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'},}

model = TableModel()
model.importDict(data)

table = TableCanvas(frame, model,editable=False)
table.createTableFrame()

master.mainloop()