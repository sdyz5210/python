#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
driver.find_element_by_id('translateContent').send_keys('hello')
driver.find_element_by_id('translateContent').submit()

time.sleep(5)
driver.quit()