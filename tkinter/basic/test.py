#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6


def test():
	import sys,Tkinter
	Tkinter.Label(text="Welcome!").pack()
	Tkinter.Button(text="Exit",command=sys.exit).pack()
	Tkinter.mainloop()

test()