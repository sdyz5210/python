#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from main import *

class Login:
	def __init__(self):
		self.root = Tk()
		usernameLabel = Label(self.root,text="用户账号:")
		usernameLabel.grid(row=0)

		self.username = StringVar()
		username_entry = Entry(self.root,width=20,textvariable=self.username)
		username_entry.grid(row=0,column=1)

		passwdLabel = Label(self.root,text="用户密码:")
		passwdLabel.grid(row=1)
		self.passwd = StringVar()
		passwd_entry = Entry(self.root,width=20,textvariable=self.passwd,show="*")
		passwd_entry.grid(row=1,column=1)

		submit_button = Button(self.root,text='登录',command=self.login,background='yellow',foreground='blue')
		submit_button.grid(row=2)
		quit_button = Button(self.root,text='退出',command=sys.exit,background='yellow',foreground='blue')
		quit_button.grid(row=2,column=1)

	def login(self):
		print self.username.get()+"--"+self.passwd.get()
		self.root.destroy()
		celloud = CelLoud()
		celloud.root.title="CelLoud客户端工具"
		celloud.root.mainloop()

if __name__ == '__main__':
	app = Login()
	app.root.mainloop()