#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.set_window_size(600,600)

#设置搜索
driver.find_element_by_id("kw").send_keys("seleniumm")
driver.find_element_by_id("su").click()
time.sleep(3)

js = "window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(3)
driver.quit()