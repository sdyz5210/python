#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

#from python_excel_utils import readExcel
from excel.python_excel_utils import *
from excel.picture_utils import *
from pymongo import MongoClient


def testExcel():
	excelList = readExcel("/Users/mac/Documents/Disease Risk.xls",True)
	client = MongoClient()
	db = client.summer
	collections = db.disease
	collections.insert(excelList)

def testPicture():
	encoded_picture = savePicture("/Users/mac/Documents/workspaces/github/python/high/a.jpg")
	client = MongoClient()
	db = client.summer
	collections = db.picture
	collections.insert({"image":encoded_picture})

readPicture()