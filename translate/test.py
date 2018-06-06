#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

content="你好"
if isinstance(content, unicode):
	content = content.encode("utf-8")
print content