#!/usr/bin/evn python
# -*- coding:utf-8 -*-
#python version 2.7.10

from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#获取输入框的大小
size = driver.find_element_by_id("kw").size
print '输入框的大小:',size

#返回百度页面底部的备案信息
text = driver.find_element_by_id("cp").text
print "打印备案信息",text

#返回元素的属性值
attribute = driver.find_element_by_id("kw").get_attribute('type')
print '元素属性值',attribute

#返回元素结果是否可见
result = driver.find_element_by_id("kw").is_displayed()
print '返回元素结果是否可见',result

time.sleep(5)
driver.quit()