#!/usr/bin/python
# -*- coding: utf-8 -*-

#http://www.cnblogs.com/way_testlife/archive/2011/04/17/2019013.html

import Image

im = Image.open("a.jpg")
#分别打印图片的原格式，高和宽的数组、颜色模式
print im.format, im.size, im.mode

#显示图片
im.show()

