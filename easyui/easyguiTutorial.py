#!/usr/bin/env python
# -*- coding: utf-8 -*-

from easygui import *

def choiceboxDemo():
	while 1:
		choices = ["Yes","No","Little"]
		reply = choicebox("你喜欢吃鱼吗?", choices=choices)

		if reply == 'Yes':
			msgbox('是的，我喜欢')
		elif reply == 'No':
			msgbox('No，我不喜欢')
		else:
			msgbox('偶尔会吃')

		if ccbox('确定要继续吗?'):
		    msgbox("我们继续")
		    continue
		else:
		    msgbox("确定要退出吗")
		    break

def msgboxDemo():
	msgbox(msg="这是一个单选按钮", title="test", ok_button="OK")

def ynboxDemo():
	ynbox(msg='yes or no',title='请选择')

def multpasswordboxDemo():
	msg = "请输入登录账号和密码"
	title = "这是一个小demo"
	fieldNames = ["账号", "密码"]
	fieldValues = []  # we start with blanks for the values
	fieldValues = multpasswordbox(msg,title, fieldNames)

	while 1:
		if fieldValues == None: 
	  		break
	  	errmsg = ""
	  	for i in range(len(fieldNames)):
	  		if fieldValues[i].strip() =="":
	      		errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
	  	if errmsg == "": 
	  		break # no problems found
	  	fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
		print "Reply was:", fieldValues

if __name__ == '__main__':
	#choiceboxDemo()
	#msgboxDemo()
	#ynbox()
	multpasswordboxDemo()