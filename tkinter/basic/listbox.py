#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

def demo1(top):
	lb = Listbox(top,selectmode = EXTENDED)
	lb.pack()
	for i in ["Python","Java","C","C++","Perl","Go"]:
		lb.insert(END,i)
def main():
	top = Tk()
	demo1(top)
	top.mainloop()

if __name__ == '__main__':
	main()