#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import Tkinter as Tk
import tktable as ta

""" AmazonBookSearchFrame"""
class AmazonBookSearchFrame(Tk.Frame):
    def __init__(self, master = None):
        Tk.Frame.__init__(self, master)
        self.master.wm_geometry("650x300+250+200")
        self.master.title(u"Amazon 本検索")

        #タイトルラベル
        titleLabel = Tk.Label(self, master, text = u"中文", font=('Helvetica', '10', 'bold'))
        titleLabel.grid(row = 0, column = 0, padx = 0, pady = 0)
        
        #タイトル入力
        self.titleStrVar = Tk.StringVar()
        self.titleInputEntry = Tk.Entry(self, textvariable = self.titleStrVar)
        self.titleInputEntry.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        # 検索ボタン
        button = Tk.Button(self, text="検索", command=self.search, width = 10)
        button.grid(row = 1, column = 1, padx = 5, pady = 5)
        
        # テーブル
        self.tableVar = ta.ArrayVar(self)
        #self.__set_table_title()
        table = ta.Table(self,
                             rows=10,
                             cols=3,
                             state='disabled',
                             width=10,
                             height=10,
                             titlerows=1,
                             colwidth=30,
                             variable=self.tableVar,
                             selecttype='row')
        table.grid(row = 2, column = 0, columnspan = 2,  sticky=Tk.W + Tk.E + Tk.N + Tk.S)
    
    def __set_table_title(self):
        titles = (u"Amazon", u"ArrayVar", u"A")
        for i in range(len(titles)):
            index = "%d,%d" % (0, i)
            self.tableVar.set(index, titles[i])
        
    def search(self):
        # 検索開始
        pass
                
if __name__ == "__main__":
    main = AmazonBookSearchFrame()
    main.pack()
    main.mainloop()