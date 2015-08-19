#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *
def mainApp(Output):
    RRColor = '#%02x%02x%02x' % (0, 73,144);
    mGui = Tk();
    mGui.title('Relational Table');
    mGui.configure(background='grey')
    text = StringVar();
    title1 = Label(mGui, text = 'Premise', fg=RRColor, borderwidth=2).grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
    title2 = Label(mGui, text = 'Conclusion', fg=RRColor, borderwidth=2).grid(row=0, column=1, sticky="nsew", padx=1, pady=1)
    title3 = Label(mGui, text = 'Support', fg=RRColor, borderwidth=2).grid(row=0, column=2, sticky="nsew", padx=1, pady=1)
    title4 = Label(mGui, text = 'Confidence', fg=RRColor, borderwidth=2).grid(row=0, column=3, sticky="nsew", padx=1, pady=1)
    title5 = Label(mGui, text = 'Lift', fg=RRColor, borderwidth=2).grid(row=0, column=4, sticky="nsew", padx=1, pady=1)
    for col in range(len(Output)):
        for row in range(len(Output[0])):
            text.set(Output[col][row])
            content = Label(mGui, textvariable=text, borderwidth=2, fg =RRColor, bg = 'white')
            content.grid(row=row+1, column=col, sticky='NSEW', padx=1, pady=1)
    mGui.mainloop()

mainApp("abcde")
