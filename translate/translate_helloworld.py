#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

from googletrans import Translator

content = Translator().translate('Hello World', dest="zh-CN").text

if isinstance(content, unicode):
    content = content.encode("utf-8")
print content