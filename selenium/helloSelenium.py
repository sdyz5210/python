#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()

#设置浏览器的宽，高显示
#driver.set_window_size(480,800)
#设置全屏显示
driver.maximize_window()

time.sleep(10)

driver.quit()