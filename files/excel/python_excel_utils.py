#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

import xlrd
import xlwt

#读取Excel工具类
#path指传递文件的路径包括文件名称，isHeader指是否存在表头
def readExcel(path,isHeader):
	list = []
	#打开excel文件
	#test '/Users/mac/Documents/疾病风险.xls'
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
			if row :
				app={}
				for j in range(colNum):
					app[colnames[j]]=row[j]
				list.append(app)
	return list

if __name__ == '__main__':
	excelList = readExcel("/Users/mac/Documents/疾病风险.xls")
	print len(excelList)