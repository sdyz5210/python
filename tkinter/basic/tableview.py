#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from ttk import *

root = Tk()

def table1():
	tree = Treeview(root)
	tree.insert('', 'end', 'widgets', text='Widget Tour')
	tree.insert('widgets', 'end', text='Canvas')
	tree.insert('', 0, 'gallery', text='Applications')
	id = tree.insert('', 'end', text='Tutorial')
	tree.insert(id, 'end', text='Tree')
	tree.pack()

def table2():
	tree = Treeview(root,columns=('SIZE', 'STATUS'))
	#tree = Treeview(root,columns=('NAME','SIZE', 'STATUS'),displaycolumns=('NAME','SIZE', 'STATUS'),show="headings")
	tree.heading("#0",text='NAME',anchor='w')
	tree.heading("#1",text='SIZE',anchor='w')
	tree.heading("#2",text='STATUS',anchor='w')
	for i in range(15):
		tree.insert('',i,text="test",value=('176','ok'))
	tree.pack()

table2()
root.mainloop()