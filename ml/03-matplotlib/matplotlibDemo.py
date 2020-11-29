#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
# 导入绘图工具包
import matplotlib.pyplot as plt

import pandas as pd

from pandas import Series, DataFrame

def test():
	N = 50
	x = np.random.rand(N)
	y = np.random.rand(N)
	colors = np.random.rand(N)
	r = 15*np.random.rand(N)
	area = np.pi *r**2

	# 绘制散点图
	plt.scatter(x, y, s=area, c=colors, alpha=0.5)
	plt.show()

def test1():
	s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))

	# 绘制线形图
	s.plot()

	plt.show()

test1()