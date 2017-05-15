#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()

def rightClick():
	driver.get("http://www.baidu.com")
	#定位到要右击的元素
	right_click = driver.find_element_by_link_text("新闻")
	ActionChains(driver).context_click(right_click).perform()

def mouseOn():
	driver.get("http://www.baidu.com")
	time.sleep(2)
	above = driver.find_element_by_link_text("设置")
	ActionChains(driver).move_to_element(above).perform()

def doubleClick():
	driver.get("http://www.baidu.com")
	double_click = driver.find_element_by_id("")
	ActionChains(driver).double_click(double_click).perform()

def dragAndDrop():
	driver.get("http://www.baidu.com")
	source = driver.find_element_by_id("xx")
	target = driver.find_element_by_id("xy")
	ActionChains(driver).drag_and_drop(source,target).perform()

if __name__ == '__main__':
	#rightClick()
	#mouseOn()
	doubleClick()
	time.sleep(2)
	driver.quit()