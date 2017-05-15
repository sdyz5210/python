#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#设置搜索
driver.find_element_by_id("kw").send_keys("seleniumm")
driver.find_element_by_id("su").click()
time.sleep(2)

#通过拍照记录错误
driver.get_screenshot_as_file("/Users/mac/Documents/data/baidu.jpg")
driver.quit()