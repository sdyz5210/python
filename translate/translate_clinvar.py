#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

import xlrd
import xlwt
import os
from googletrans import Translator


def writeExcel(rows,fileName,extension):
	workbook = xlwt.Workbook(encoding = 'utf-8')
	table = workbook.add_sheet(fileName)
	fileName = fileName+"_translate"+extension
	if fileName=='PubMed':
		for i in range(len(rows)):
			table.write(i,0,rows[i][0])
			table.write(i,1,rows[i][1])
			table.write(i,2,rows[i][2])
	elif fileName=="SummaryEvidence":
		for i in range(len(rows)):
			table.write(i,0,rows[i][0])
			table.write(i,1,rows[i][1])
			table.write(i,2,rows[i][2])
	elif fileName=="SupportingObservations":
		for i in range(len(rows)):
			table.write(i,0,rows[i][0])
			table.write(i,1,rows[i][1])
			table.write(i,2,rows[i][2])
			table.write(i,3,rows[i][3])
			table.write(i,4,rows[i][4])
	workbook.save(fileName)

#读取Excel工具类
#path指传递文件的路径包括文件名称，isHeader指是否存在表头
'''
	path:指传递文件的路径包括文件名称
	fileName:文件名
	extension:文件后缀
	isHeader:是否存在表头

	VariationID	Abstract
'''
def readExcel(path,fileName,extension,isHeader):
	#打开excel文件
	rows=[]
	with xlrd.open_workbook(path) as data:
		#根据索引顺序-获取工作sheets
		sheets1 = data.sheets()[0]
		#获取行列的值
		#获取行数和列数
		rowNum = sheets1.nrows
		colNum = sheets1.ncols
		colnames =  sheets1.row_values(0)
		print "行数:%d,列数:%d",(rowNum,colNum)
		if fileName=='PubMed':
			for i in range(rowNum):
				row = sheets1.row_values(i)
				if isHeader and (i == 0):
					temp = [row[0],row[1],"Abstract_zh"]
					rows.append(temp)
					continue
				row = sheets1.row_values(i)
				print "当前行号为:%d,id号为:%s",(i,row[0])
				Abstract_zh = translateTozh(row[1])
				temp = [row[0],row[1],Abstract_zh]
				rows.append(temp)
		elif fileName=="SummaryEvidence":
			for i in range(rowNum):
				row = sheets1.row_values(i)
				if isHeader and (i == 0):
					temp = [row[0],row[1],"FullDescription_zh"]
					rows.append(temp)
					continue
				row = sheets1.row_values(i)
				print "当前行号为:%d,id号为:%s",(i,row[0])
				FullDescription_zh = translateTozh(row[1])
				temp = [row[0],row[1],FullDescription_zh]
				rows.append(temp)
		elif fileName=="SupportingObservations":
			#Description	FullDescription
			for i in range(rowNum):
				row = sheets1.row_values(i)
				if isHeader and (i == 0):
					temp = [row[0],row[1],"Description_zh",row[2],"FullDescription_zh"]
					rows.append(temp)
					continue
				row = sheets1.row_values(i)
				print "当前行号为:%d,id号为:%s",(i,row[0])
				Description_zh = translateTozh(row[1])
				FullDescription_zh = translateTozh(row[2])
				temp = [row[0],row[1],Description_zh,row[2],FullDescription_zh]
				rows.append(temp)
	writeExcel(rows,fileName,extension)

def translateTozh(content):
	translator = Translator()
	content_zh = ""
	try:
		content_zh = translator.translate(content, dest="zh-CN").text
		if isinstance(content_zh, unicode):
			content_zh = content_zh.encode("utf-8")
	except Exception, e:
		pass
	return content_zh

'''
	批量进行翻译时执行该脚本
'''
def readFileList():
	for i in range(1,13):
		filePath = "Well"+str(i)+".xlsx"
		fileName = os.path.splitext(filePath)[0]
		extension = os.path.splitext(filePath)[1]
		readExcel(filePath,fileName,extension,True)

if __name__ == '__main__':
	#readFileList()
	readExcel("PubMed.xlsx","PubMed",".xlsx",True)
	readExcel("SummaryEvidence.xlsx","SummaryEvidence",".xlsx",True)
	readExcel("SupportingObservations.xlsx","SupportingObservations",".xlsx",True)