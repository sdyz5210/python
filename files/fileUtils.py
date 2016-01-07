#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import os,hashlib,datetime,logging

logging.basicConfig(filename = "md5.log",level = logging.INFO,format='[%(asctime)s %(levelname)s] %(message)s',datefmt='%Y%m%d %H:%M:%S')

#计算大文件的MD5
def getBigFileMD5(filePath):
	m = hashlib.md5()
	with open(filePath,"rb") as f:
		while True:
			data = f.read(8096)
			if not data:
				break
			m.update(data)
	return m.hexdigest()

#获取某个目录下文件列表
def getFileList(targetDir):
	fileDict = {}
	fileList = os.listdir(targetDir)
	for i in fileList:
		filepath = os.path.join(targetDir,i)
		if os.path.isfile(filepath):
			md5 = getBigFileMD5(filepath)
			fileDict[i.split('.')[0]] = md5
	with open('fileMd5.txt','a') as f:
		for key,value in fileDict.items():
			f.write(key+","+value+'\n')
			f.flush()

if __name__ == '__main__':
	startTime = datetime.datetime.now()
	getFileList('/share/data/file/')
	endTime = datetime.datetime.now()
	t = (endTime-startTime).total_seconds()
	logging.info('本次运行的时间---v5:'+str(t))