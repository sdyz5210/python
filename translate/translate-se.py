#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

import xlrd
import xlwt
from googletrans import Translator

'''
	主要完成对SummaryEvidence文件的翻译
'''

translator = Translator()

def writeExcel(rows):
	workbook = xlwt.Workbook(encoding = 'utf-8')
	table = workbook.add_sheet("SummaryEvidence")
	for i in range(len(rows)):
		table.write(i,0,rows[i][0])
		table.write(i,1,rows[i][1])
		table.write(i,2,rows[i][2])
	workbook.save('SummaryEvidence-translate.xls')

#读取Excel工具类
#path指传递文件的路径包括文件名称，isHeader指是否存在表头
def readExcel(path,isHeader):
	#打开excel文件
	#test '/Users/mac/Documents/PubMed.xlsx'
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
		for i in range(rowNum):
			if isHeader and (i == 0):
				continue
			row = sheets1.row_values(i)
			print "当前行号为:%d,id号为:%s",(i,row[0])
			content_zh = ""
			try:
				content_zh = translator.translate(row[1], dest="zh-CN").text
				if isinstance(content_zh, unicode):
					content_zh = content_zh.encode("utf-8")
				temp = [row[0],row[1],content_zh]
				rows.append(temp)
			except Exception, e:
				temp = [row[0],row[1],""]
				rows.append(temp)
			continue
	writeExcel(rows)

if __name__ == '__main__':
	readExcel("SummaryEvidence.xlsx",True)