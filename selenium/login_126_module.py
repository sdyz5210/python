#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
import time

driver =  webdriver.Firefox()
driver.get("http://mail.126.com")
#设置隐士等待10s
driver.implicitly_wait(10)

def login():
	driver.switch_to.frame("x-URS-iframe")
	driver.find_element_by_name("email").clear()
	driver.find_element_by_name("email").send_keys("username")
	driver.find_element_by_name("password").clear()
	driver.find_element_by_name("password").send_keys("password")
	driver.find_element_by_id("dologin").click()

def logout():
	driver.switch_to_default_content()
	#driver.find_element_by_link_text(u"退出").click()	#success
	#driver.find_element_by_xpath("/html/body/header/div/ul/li[18]/a").click()	#success
	driver.find_element_by_xpath("//ul[@id='_mail_component_6_6']/li[18]/a").click()	#success
	#driver.find_element_by_xpath("//li[@id='_mail_component_41_41']/a").click()	#success

login()
time.sleep(3)
logout()
driver.quit()
