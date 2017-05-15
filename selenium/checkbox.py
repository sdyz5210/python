#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

'''
定位一组元素

find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()

'''

from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

def toCheck():
	inputs = driver.find_elements_by_tag_name("input")

	for i in inputs:
		if i.get_attribute('type')=='checkbox':
			i.click()
			time.sleep(1)

def toChecked():
	#通过xpath查找
	checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")
	#通过css查找
	checkboxs = driver.find_elements_by_css_selector("input[type=checkbox]")
	for checkbox in checkboxs:
		checkbox.click()
		time.sleep(1)
	print len(checkboxs)
	#取消最后一个checkbox选中状态。pop默认返回最后一个，返回第2个为：pop(1)
	driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
	time.sleep(1)

if __name__ == '__main__':
	toChecked()
	driver.quit()