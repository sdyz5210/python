#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
from tkFileDialog import askopenfilenames
import tkMessageBox

tk=Tk()
tk.withdraw()

def fileupload():
    while True:
        uploadedfilenames = askopenfilenames(multiple=True)
        if uploadedfilenames == '':
            tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
            return
        uploadedfiles = tk.splitlist(uploadedfilenames)
        if len(uploadedfiles)!=2:
           tkMessageBox.showinfo(message="2 files have not been selected!")
        else:
            return uploadedfiles

print fileupload()