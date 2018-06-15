#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

import xlrd
import xlwt
import os
from googletrans import Translator

'''
	主要完成对omim-percentage文件的翻译，需要翻译文件的表头为：
	0、OMIMID	
	1、url	
	2、GENENAME	
	3、AlternativeTitles	
	4、HGNCApprovedGeneSymbol	
	5、CytogeneticLocation	
	6、GenomicCoordinates	
	7、Description--------------zh
	8、CloningAndExpression-----zh
	9、GeneStructure	------------zh
	10、Mapping-----------------zh
	11、BiochemicalFeatures-----zh
	12、GeneFunction	------------zh
	13、MolecularGenetics-------zh
	14、GenotypePhenotypeCorrelations---zh	
	15、AnimalModel-------------zh
	文件的表头列数为：16，翻译后为25列
'''

def writeExcel(rows,fileName,extension):
	workbook = xlwt.Workbook(encoding = 'utf-8')
	table = workbook.add_sheet(fileName)
	fileName = fileName+"_translate"+extension
	for i in range(len(rows)):
		table.write(i,0,rows[i][0])
		table.write(i,1,rows[i][1])
		table.write(i,2,rows[i][2])
		table.write(i,3,rows[i][3])
		table.write(i,4,rows[i][4])
		table.write(i,5,rows[i][5])
		table.write(i,6,rows[i][6])
		table.write(i,7,rows[i][7])
		table.write(i,8,rows[i][8])
		table.write(i,9,rows[i][9])
		table.write(i,10,rows[i][10])
		table.write(i,11,rows[i][11])
		table.write(i,12,rows[i][12])
		table.write(i,13,rows[i][13])
		table.write(i,14,rows[i][14])
		table.write(i,15,rows[i][15])
		table.write(i,16,rows[i][16])
		table.write(i,17,rows[i][17])
		table.write(i,18,rows[i][18])
		table.write(i,19,rows[i][19])
		table.write(i,20,rows[i][20])
		table.write(i,21,rows[i][21])
		table.write(i,22,rows[i][22])
		table.write(i,23,rows[i][23])
		table.write(i,24,rows[i][24])
	workbook.save(fileName)

#读取Excel工具类
#path指传递文件的路径包括文件名称，isHeader指是否存在表头
'''
	path:指传递文件的路径包括文件名称
	fileName:文件名
	extension:文件后缀
	isHeader:是否存在表头
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
		for i in range(rowNum):
			row = sheets1.row_values(i)
			if isHeader and (i == 0):
				temp = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],"Description_zh",row[8],"CloningAndExpression_zh",row[9],"GeneStructure_zh",row[10],"Mapping_zh",row[11],"BiochemicalFeatures_zh",row[12],"GeneFunction_zh",row[13],"MolecularGenetics_zh",row[14],"GenotypePhenotypeCorrelations_zh",row[15],"AnimalModel_zh"]
				rows.append(temp)
				continue
			row = sheets1.row_values(i)
			print "当前行号为:%d,id号为:%s",(i,row[0])
			Description_zh = translateTozh(row[7])
			CloningAndExpression_zh = translateTozh(row[8])
			GeneStructure_zh = translateTozh(row[9])
			Mapping_zh = translateTozh(row[10])
			BiochemicalFeatures_zh = translateTozh(row[11])
			GeneFunction_zh = translateTozh(row[12])
			MolecularGenetics_zh = translateTozh(row[13])
			GenotypePhenotypeCorrelations_zh = translateTozh(row[14])
			AnimalModel_zh = translateTozh(row[15])
			temp = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],Description_zh,row[8],CloningAndExpression_zh,row[9],GeneStructure_zh,row[10],Mapping_zh,row[11],BiochemicalFeatures_zh,row[12],GeneFunction_zh,row[13],MolecularGenetics_zh,row[14],GenotypePhenotypeCorrelations_zh,row[15],AnimalModel_zh]
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

def readFileList():
	for i in range(1,13):
		filePath = "Plus"+str(i)+".xlsx"
		fileName = os.path.splitext(filePath)[0]
		extension = os.path.splitext(filePath)[1]
		readExcel(filePath,fileName,extension,True)

if __name__ == '__main__':
	readFileList()