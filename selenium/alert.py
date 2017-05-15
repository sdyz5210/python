#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os,time
import sys

'''
	这个例子没有走通，因为find_elements_by_link_text 在百度页面现在获取不到元素信息。
	ActionChains一直没有执行
'''

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

links = driver.find_elements_by_link_text("设置")
for link in links:
	if link.is_displayed():
		ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
sets = driver.find_elements_by_link_text("搜索设置")
for s in sets:
	if s.is_displayed():
		s.click()

#保存设置
saves = driver.find_elements_by_class_name("prefpanelgo")
for save in saves:
	if save.is_displayed():
		save.click()

time.sleep(2)

driver.switch_to_alert().accept()

driver.quit()