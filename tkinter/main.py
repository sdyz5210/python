#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from tkFileDialog import *
from ttk import *
import tkMessageBox
import os

class CelLoud:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("800x500")
		self.button = Button(self.root,text="选择文件",command=self.getFileList)
		self.button.pack()
		
		self.tree = Treeview(self.root,columns=(u'文件名称', u'文件大小', u'文件类型'))
		self.tree.heading("#0",text=u'序号',anchor='w')
		self.tree.heading("#1",text=u'文件名称',anchor='w')
		self.tree.heading("#2",text=u'文件大小',anchor='w')
		self.tree.heading("#3",text=u'文件类型',anchor='w')
		self.tree.pack()

	def fillTable(self):
		for i in range(len(self.list)):
			fd = self.list[i]
			self.tree.insert('',i,text=i,value=(fd.fileName,fd.fileSize,fd.fileTypes))

	def getFileList(self):
		self.list = []
		uploadedfilenames = askopenfilenames(multiple=True,filetypes=[('GIF FILES', '*.gif'),('PY FILES','*.py')])
		uploadedfiles = self.root.tk.splitlist(uploadedfilenames)
		for i in range(len(uploadedfiles)):
			fName = os.path.basename(uploadedfiles[i])
			fSize = os.path.getsize(uploadedfiles[i])
			fPath = uploadedfiles[i]
			fTypes = os.path.splitext(uploadedfiles[i])[1]
			fd = FileData(fName,fPath,fSize,fTypes)
			fd.display()
			self.list.append(fd)
		self.fillTable()


class FileData:
	fileName = ""
	filePath = ""
	fileSize = ""
	fileTypes = ""
	def __init__(self,fileName,filePath,fileSize,fileTypes):
		self.fileName = fileName
		self.fileSize = fileSize
		self.filePath = filePath
		self.fileTypes = fileTypes

	def display(self):
		print "fileName : ", self.fileName,  ", fileSize: ", self.fileSize, ", fileTypes: ", self.fileTypes

if __name__ == '__main__':
	celloud = CelLoud()
	celloud.root.mainloop()