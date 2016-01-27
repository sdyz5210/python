#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import * 
from tkintertable import TableCanvas, TableModel

data = {'rec1': {'col1': 99, 'col2': 108, 'label': 'rec1'},
			'rec2': {'col1': 90, 'col2': 79, 'label': 'rec2'},
			'rec3': {'col1': 88, 'col2': 90, 'label': 'rec3'}}

#创建一个表格
def demo1(root):
	frame = Frame(root)
	frame.pack()
	table = TableCanvas(frame)
	table.createTableFrame()

#创建表格，并为表格绑定数据模型
def demo2(root):
	frame = Frame(root)
	frame.pack()
	model = TableModel()
	model.importDict(data)
	table = TableCanvas(frame, model=model)
	table.createTableFrame()

#修改表格的数据
def demo3(root):
	frame = Frame(root)
	frame.pack()
	model = TableModel()
	model.importDict(data)
	table = TableCanvas(frame, model=model)
	table.createTableFrame()
	table.model.data['rec2']['col2'] = 50
	table.redrawTable()

#表格参数熟悉
#showkeynamesinheader 设置左侧序号显示
#rowheaderwidth 设置最左侧的列是否显示
#cellwidth 设置单元格的宽度
#rowheight 设置单元格的高度
#editable=False 设置单元格是否可以编辑
#thefont="Arial 10" 设置字体
#cellbackgr='#E3F6CE' 设置单元格背景颜色
#rowselectedcolor='yellow' 设置行被选中时的背景颜色
#reverseorder=1 倒序，但具体没有试验出效果
def demo4(root):
	frame = Frame(root)
	frame.pack()
	model = TableModel()
	model.importDict(data)
	table = TableCanvas(frame, model=model,rowheaderwidth=0,cellwidth=150,rowheight=20,editable=False,rowselectedcolor='red',reverseorder=1)
	table.createTableFrame()

def demo5(root):
	frame = Frame(root)
	frame.pack()
	table = TableCanvas(frame,rowheaderwidth=0,cellwidth=150,rowheight=20,editable=False,rowselectedcolor='red',reverseorder=1)
	table.createTableFrame()

def createData():
	pass

def main():
	root = Tk()
	demo5(root)
	root.mainloop()

if __name__ == '__main__':
	main()