#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get('http://cuiqingcai.com')
print type(r)
# http 状态码
print r.status_code
# 页面编码
print r.encoding
# 页面响应 -- 内容较多，占时隐藏掉
# print r.text
# cookies的信息
print r.cookies