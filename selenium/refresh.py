#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
time.sleep(2)

driver.refresh()
time.sleep(2)
driver.quit()