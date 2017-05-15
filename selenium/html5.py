#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://videojs.com')
video = driver.find_element_by_id("preview-player_html5_api")

#返回播放文件地址--
url = driver.execute_script("return arguments[0].currentSrc;",video)
print url

#播放视频
print "start"
driver.execute_script("return arguments[0].play()",video)
time.sleep(15)

#暂停视频
driver.execute_script("return arguments[0].pause()",video)

driver.quit()