#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

def login(driver,username,password):
	driver.switch_to.frame("x-URS-iframe")
	driver.find_element_by_name("email").clear()
	driver.find_element_by_name("email").send_keys(username)
	driver.find_element_by_name("password").clear()
	driver.find_element_by_name("password").send_keys(password)
	driver.find_element_by_id("dologin").click()

def logout(driver):
	driver.switch_to_default_content()
	driver.find_element_by_link_text(u"退出").click()