#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def test5():
	# 每行的后一个值减去前一个，然后放到一个新的数组里面
	a5 = np.array([1,7,3,6,10,10])
	print a5
	a5 = np.diff(a5)
	print a5
	a5 = np.sign(a5)
	print a5
test5()
def test4():
	a5 = np.array([[1,1],[2,2],[3,3],[4,4],[5,5]])
	print a5
	temp=np.insert(a5,0,"-inf")
	temp=np.append(temp,"-inf")
	temp = temp.astype("float64")
	print temp

def test3():
	a4 = np.arange(12)
	print a4
	print a4.reshape(4, 3)

def test2():	
	# 元素值为0-3数组
	a3 = np.arange(4)
	# [0 1 2 3]
	a3
	# 查看维数---1
	a3.ndim

	a3.shape

	# 元素值为0-3数组一维数组
	np.arange(4)
	np.ones((4, 4), dtype=np.int64)
	# 元素值全为0 2x2数组
	np.zeros((2, 2))
	
	np.empty((3, 3), dtype=np.int64)
	np.ones((4, 3, 4))

def test1():
	# 一维数组 
	a1 = np.array([1, 2, 3, 4])

	# [1 2 3 4]
	a1

	# 多维数组各个维度的大小,返回一个元组---(4,)
	a1.shape

	# 数组里面元素个数---4
	a1.size

	# 数组中数据类型---int64
	a1.dtype

	# 二维数组
	a2 = np.array([[1.0, 2.5, 3], [0.5, 4, 9]])

	# (2, 3) 6 float64
	a2.shape,a2.size,a2.dtype

	# 0.5
	a2.min()

	# 数组类型为ndarray--<type 'numpy.ndarray'>
	type(a1)