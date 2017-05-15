#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
import time

driver =  webdriver.Firefox()

driver.get("https://www.celloud.cn/login")

driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")

driver.find_element_by_id("loginBtn").click()

time.sleep(5)
driver.quit()