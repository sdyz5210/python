#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver =  webdriver.Firefox()
driver.get("http://www.baidu.cn")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(1)

#删除多输入的字符m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(1)

#输入空格加教程
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("tutorial")
time.sleep(1)

#全选输入的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(1)
#剪切输入的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(1)
#黏贴输入的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(1)

#执行回车
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(1)
driver.quit()
