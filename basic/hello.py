#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('text.txt','a') as f:
	for i,c in enumerate('abckslssdfadfkskfkkdkfkjd'):
		f.writelines(str(i))