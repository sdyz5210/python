#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
import os

# 旋转
# img.rotate(90).show()

# 定义需要处理images的目录
workDir = "/Users/mac/Documents/workspaces/github/python/office/test02/"
# 获取当前目录所有的文件列表
fileNames = os.listdir(workDir)
size = 300,300
# 循环遍历逐一读取image文件
for fileName in fileNames:
    # 获取当前文件的绝对路径
    imgPath = os.path.join(workDir,fileName)
    img = Image.open(imgPath)

    # resize成300*300像素大小。  
    img = img.resize(size)
    img.save(os.path.join(workDir,"new_"+fileName))