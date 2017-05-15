#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath('frame.html')
driver.get(file_path)

#切换到iframe中
driver.switch_to.frame("if")
#还可以切换到上层页面
#driver.switch_to.parent_frame()

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

driver.quit()