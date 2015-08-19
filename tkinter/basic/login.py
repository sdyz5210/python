#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
import sys

root = Tk()
root.title("请登录")

def login():
	print username.get()+"--"+passwd.get()
	root.destory()

usernameLabel = Label(root,text="用户账号:")
usernameLabel.grid(row=0)

username = StringVar()
username_entry = Entry(root,width=20,textvariable=username)
username_entry.grid(row=0,column=1)

passwdLabel = Label(root,text="用户密码:")
passwdLabel.grid(row=1)
passwd = StringVar()
passwd_entry = Entry(root,width=20,textvariable=passwd,show="*")
passwd_entry.grid(row=1,column=1)

submit_button = Button(root,text='登录',command=login,background='yellow',foreground='blue')
submit_button.grid(row=2)
quit_button = Button(root,text='退出',command=sys.exit,background='yellow',foreground='blue')
quit_button.grid(row=2,column=1)
root.mainloop()

def tologin3():
	root.title("请登录")
	frame = Frame(root)
	frame.pack(side='top',padx=10,pady=20,anchor='w')
	
	usernameLabel = Label(frame,text="用户账号:")
	usernameLabel.pack(side='left')

	username = StringVar()
	username_entry = Entry(frame,width=20,textvariable=username)
	username_entry.pack(side='left')

	frame = Frame(root)
	frame.pack(side='top',padx=10,pady=20,anchor='w')

	passwdLabel = Label(frame,text="用户密码:")
	passwdLabel.pack(side='left')

	passwd = StringVar()
	passwd_entry = Entry(frame,width=20,textvariable=passwd)
	passwd_entry.pack(side='left')

	frame = Frame(root)
	frame.pack(side='top',padx=10,pady=20,anchor='w')

	submit_button = Button(frame,text='登录',command=login,background='yellow',foreground='blue')
	submit_button.pack(side='right', pady=5, ipadx=30, ipady=30, anchor='w')
	quit_button = Button(frame,text='退出',command=sys.exit,background='yellow',foreground='blue')
	quit_button.pack(side='left', pady=5, ipadx=30, ipady=30, anchor='w')
	root.mainloop()

def tologin1():
	root.title("请登录")
	m1 = PanedWindow(root,orient=VERTICAL)
	m1.pack(fill=BOTH, expand=1)

	frame = Frame(m1)
	frame.pack(side='top',padx=10,pady=20,anchor='w')
	
	usernameLabel = Label(frame,text="用户账号:")
	usernameLabel.pack(side='left')

	username = StringVar()
	username_entry = Entry(frame,width=20,textvariable=username)
	username_entry.pack(side='left')

	m1.add(frame)

	frame = Frame(m1)
	frame.pack(side='top',padx=10,pady=20,anchor='w')

	passwdLabel = Label(frame,text="用户密码:")
	passwdLabel.pack(side='left')

	passwd = StringVar()
	passwd_entry = Entry(frame,width=20,textvariable=passwd)
	passwd_entry.pack(side='left')

	m1.add(frame)

	frame = Frame(m1)
	frame.pack(side='top',padx=10,pady=20,anchor='w')

	submit_button = Button(frame,text='登录',command=login,background='yellow',foreground='blue')
	submit_button.pack(side='left', pady=5, ipadx=30, ipady=30, anchor='w')
	quit_button = Button(frame,text='退出',command=sys.exit,background='yellow',foreground='blue')
	quit_button.pack(side='left', pady=5, ipadx=30, ipady=30, anchor='w')

	m1.add(frame)
	root.mainloop()