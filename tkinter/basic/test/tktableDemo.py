#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6
from Tkinter import *
from TkTreectrl import *
import sqlite3

def main():
    root = Tk()
    root.title('Simple MultiListbox demo')
    mlb = TkTreectrl.MultiListbox(root)
    mlb.pack(side='top', fill='both', expand=1)
    Button(root, text='Close', command=root.quit).pack(side='top', pady=5)
    mlb.focus_set()   
    mlb.configure(selectcmd=select_cmd, selectmode='extended')
    mlb.config(columns=('Column 1', 'Column 2'))
 	maps = [('Hyundai', 'brakes')]  
    for row in maps:
        mlb.insert('end',row)
    root.mainloop()

if __name__=='__main__':
    main()