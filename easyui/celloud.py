#!/usr/bin/env python
# -*- coding: utf-8 -*-

from easygui import *

def loginPanel():
	title = 'CelLoud客户端上传工具'
	msg = "请输入您的用户名和密码:"
	fieldNames = ["登录账号","登录密码"]
	fieldValues = []  # we start with blanks for the values
	fieldValues = multenterbox(msg,title, fieldNames)

	# make sure that none of the fields was left blank
	while 1:
	    if fieldValues == None: break
	    errmsg = ""
	    for i in range(len(fieldNames)):
	      if fieldValues[i].strip() == "":
	        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
	    if errmsg == "": break # no problems found
	    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	print "Reply was:", fieldValues

def main():
	pass

if __name__ == '__main__':
	loginPanel()