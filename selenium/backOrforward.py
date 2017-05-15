#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()

firstUrl = "http://www.baidu.com"
print "now access ",firstUrl
driver.get(firstUrl)

time.sleep(2)
secondUrl = "http://news.baidu.com"
print "now access ",secondUrl
driver.get(secondUrl)

time.sleep(2)
print "back to ",firstUrl
driver.back()

time.sleep(2)
print "forward to ",secondUrl
driver.forward()

time.sleep(2)
driver.quit()