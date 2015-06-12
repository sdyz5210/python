#!/usr/bin/env python
#-*- coding: utf-8 -*-

import httplib

httpClient = None

try:
	httpClient = httplib.HTTPConnection('www.python.org')
	httpClient.request('HEAD','/index.html')

	response = httpClient.getresponse()
	print response.status
	print response.reason
	print response.read()
except Exception, e:
	print e
finally:
	if httpClient:
		httpClient.close()