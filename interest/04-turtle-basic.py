#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.x

from turtle import *
import time

def drawSunFlower():
	#同时设置pencolor=red, fillcolor=yellow
	#t.color("red", "yellow")

	# 也可以分开设置
	pencolor("red")
	fillcolor("yellow")

	#设置画的速度
	speed(5)
	# 开始准备填充图形
	begin_fill()
	for i in range(50):
		# 向当前画笔方向移动200像素长
		forward(200)
		# 逆时针移动170°
		left(170)
	#填充完成
	end_fill()
	time.sleep(1)

def drawSnake():
	# 设置画布大小
	setup(1500, 1400, 0, 0)
	# 画笔尺寸
	pensize(30)
	# 画笔颜色
	pencolor("green")
	# 前进的方向
	seth(-40)
	rad = 70
	angle = 80
	length = 2
	neckrad = 15
	for _ in range(length):
		circle(rad, angle)
		circle(-rad, angle)
	circle(rad, angle/2)
	forward(rad/2)  # 直线前进
	circle(neckrad, 180)
	forward(rad/4)


def drawStar():
	pensize(5)
	pencolor("yellow")
	fillcolor("red")
	begin_fill()

	for _ in range(5):
		forward(200)
		right(144)
	end_fill()
	time.sleep(2)

	penup()
	goto(-150,-120)
	color("violet")
	write("Done", font=('Arial', 40, 'normal'))
	time.sleep(1)

if __name__ == '__main__':
	# drawSunFlower()
	# drawSnake()
	drawStar()