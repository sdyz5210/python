#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

from python_excel_utils import readExcel
from pymongo import MongoClient

excelList = readExcel("/Users/mac/Documents/疾病风险.xls",True)

client = MongoClient()
db = client.summer
collections = db.disease
collections.insert(excelList)