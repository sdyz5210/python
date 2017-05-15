#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
cookie = driver.get_cookies()
print cookie

driver.add_cookie({'name':'key_123',"value":'value_123'})
cookie = driver.get_cookies()
print cookie
driver.quit()