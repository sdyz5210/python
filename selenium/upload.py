#!/usr/bin/evn python
# -*- coding:UTF-8 -*-
# python version 2.7.10

from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path = "file:///"+os.path.abspath("upload.html")
driver.get(file_path)

driver.find_element_by_name("file").send_keys("/Users/mac/Documents/data/ab1/test.txt")

time.sleep(3)
driver.quit()