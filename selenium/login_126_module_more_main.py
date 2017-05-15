#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
import time
import login_126_module_more_public as public

driver =  webdriver.Firefox()
#设置隐士等待10s
driver.implicitly_wait(10)
driver.get("http://mail.126.com")

class Account(object):
	def __init__(self, username,password):
		self.username = username
		self.password = password

account = Account("username","password")
public.login(driver,account)
public.logout(driver)
driver.quit()