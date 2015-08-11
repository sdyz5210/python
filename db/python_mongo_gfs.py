#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python v2.7.6

from pymongo import MongoClient
import gridfs

db = MongoClient().summergfs
fs = gridfs.GridFS(db)
fs.put("/Users/mac/Documents/workspaces/github/python/high/a.jpg")