#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
baidu_url = "http://www.baidu.com"
#设置隐士等待10s
driver.implicitly_wait(10)
driver.get(baidu_url)

#获取百度搜索窗口句柄
search_windows=driver.current_window_handle

#下面两句会抛出元素不可见异常
#driver.find_element_by_link_text('登录').click()
#driver.find_element_by_link_text("立即注册").click()
#所以按照下面的方式进行

logins = driver.find_elements_by_link_text('登录')
for login in logins:
	if login.is_displayed():
		login.click()

registers = driver.find_elements_by_link_text("立即注册")
for register in registers:
	if register.is_displayed():
		register.click()

#获取当前所有打开的窗口的句柄
all_handles = driver.window_handles

#进入注册页面
for handle in all_handles:
	if handle != search_windows:
		driver.switch_to.window(handle)
		print "注册页面"
		driver.find_element_by_name("account").send_keys("username")
		driver.find_element_by_name("password").send_keys("password")
		time.sleep(2)

#回到搜索页面
for handle in all_handles:
	if handle == search_windows:
		driver.switch_to.window(handle)
		print "搜索页面"
		driver.find_element_by_id("TANGRAM__PSP_2__closeBtn").click()
		driver.find_element_by_id("kw").send_keys("selenium")
		driver.find_element_by_id("su").click()
		time.sleep(5)

driver.quit()

'''
current_window_handle 获得当前窗口句柄
window_handles 返回所有窗口的句柄到当前回话
switch_to.window() 用于切换到相应的窗口。
'''