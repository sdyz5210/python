#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import os
from tktable import *
from Tkinter import *

root = Tk()

fileDir = '/Users/mac/Documents/data/bam'
l = os.listdir(fileDir)
fileVar = []
for i in l:
	filePath = os.path.join(fileDir,i)
	fileSize = os.path.getsize(filePath)
	fl = [i,filePath,fileSize]
	fileVar.append(fl)
var = ArrayVar(root)
i = 0
for row in fileVar:
	j = 0
	for cell in row:
		index = "%i,%i" % (i, j)
		var[index] = cell
		j += 1
	i += 1
test = Table(root,rows=10,cols=5,
			state='disabled',
			width=6,
			height=6,
			titlerows=0,
			titlecols=0,
			roworigin=0,
			colorigin=0,
			selectmode='browse',
			selecttype='row',
			rowstretch='unset',
			colstretch='last',
			#browsecmd=browsecmd,
			flashmode='on',
			variable=var,
			usecommand=0)
test.pack(expand=1, fill='both')
root.mainloop()