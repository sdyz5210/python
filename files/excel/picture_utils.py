#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

import base64
from pymongo import MongoClient
from bson.objectid import ObjectId

def savePicture(path):
	encoded_picture=''
	with open(path,"rb") as pic:
		encoded_picture = base64.b64encode(pic.read())
	return encoded_picture

def readPicture():
	client = MongoClient()
	db = client.summer
	collections = db.picture
	map = collections.find_one({"_id":ObjectId("55c88eec6f4aa8432c092700")})
	for k,v in map.items():
		print (k,v)