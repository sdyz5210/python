#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

from Tkinter import *

def new_file():
    print "Open new file"

def open_file():
    print "Open existing file"

def stub_action():
    print "Menu select"

def makeCommandMenu():
    CmdBtn = Menubutton(mBar, text='Button Commands', underline=0)
    CmdBtn.pack(side=LEFT, padx="2m")
    CmdBtn.menu = Menu(CmdBtn)

    CmdBtn.menu.add_command(label="Undo")
    CmdBtn.menu.entryconfig(0, state=DISABLED)
    CmdBtn.menu.add_command(label='New...', underline=0, command=new_file)
    CmdBtn.menu.add_command(label='Open...', underline=0, command=open_file)
    CmdBtn.menu.add_command(label='Wild Font', underline=0,
    font=('Tempus Sans ITC', 14), command=stub_action)
    CmdBtn.menu.add_command(bitmap="@bitmaps/RotateLeft")
    CmdBtn.menu.add('separator')
    CmdBtn.menu.add_command(label='Quit', underline=0, 
    background='white', activebackground='green', 
    command=CmdBtn.quit)

    CmdBtn['menu'] = CmdBtn.menu
    return CmdBtn

def makeCascadeMenu():
    CasBtn = Menubutton(mBar, text='Cascading Menus', underline=0)
    CasBtn.pack(side=LEFT, padx="2m")
    CasBtn.menu = Menu(CasBtn)
    CasBtn.menu.choices = Menu(CasBtn.menu)
    CasBtn.menu.choices.wierdones = Menu(CasBtn.menu.choices)

    CasBtn.menu.choices.wierdones.add_command(label='A')
    CasBtn.menu.choices.wierdones.add_command(label='B')
    CasBtn.menu.choices.wierdones.add_command(label='C')
    CasBtn.menu.choices.wierdones.add_command(label='D')    

    CasBtn.menu.choices.add_command(label='A')
    CasBtn.menu.choices.add_command(label='B')
    CasBtn.menu.choices.add_command(label='C')
    CasBtn.menu.choices.add_command(label='D')
    CasBtn.menu.choices.add_command(label='E')
    CasBtn.menu.choices.add_command(label='F')
    CasBtn.menu.choices.add_cascade(label='G', menu=CasBtn.menu.choices.wierdones)

    CasBtn.menu.add_cascade(label='Scipts', menu=CasBtn.menu.choices)
    CasBtn['menu'] = CasBtn.menu
    return CasBtn

def makeCheckbuttonMenu():
    ChkBtn = Menubutton(mBar, text='Checkbutton Menus', underline=0)
    ChkBtn.pack(side=LEFT, padx='2m')
    ChkBtn.menu = Menu(ChkBtn)

    ChkBtn.menu.add_checkbutton(label='A')
    ChkBtn.menu.add_checkbutton(label='B')
    ChkBtn.menu.add_checkbutton(label="C")
    ChkBtn.menu.add_checkbutton(label='D')
    ChkBtn.menu.add_checkbutton(label='E')    
    ChkBtn.menu.invoke(ChkBtn.menu.index('C'))

    ChkBtn['menu'] = ChkBtn.menu
    return ChkBtn

def makeRadiobuttonMenu():
    RadBtn = Menubutton(mBar, text='Radiobutton Menus', underline=0)
    RadBtn.pack(side=LEFT, padx='2m')
    RadBtn.menu = Menu(RadBtn)

    RadBtn.menu.add_radiobutton(label='A')
    RadBtn.menu.add_radiobutton(label='B')
    RadBtn.menu.add_radiobutton(label='C')
    RadBtn.menu.add_radiobutton(label='D')
    RadBtn.menu.add_radiobutton(label='E')
    RadBtn.menu.add_radiobutton(label='F')
    RadBtn.menu.add_radiobutton(label='G')
    RadBtn.menu.add_radiobutton(label='H')
    RadBtn.menu.add_radiobutton(label='I')
    RadBtn['menu'] = RadBtn.menu
    return RadBtn


def makeDisabledMenu(): 
    Dummy_button = Menubutton(mBar, text='Disabled Menu', underline=0)
    Dummy_button.pack(side=LEFT, padx='2m')
    Dummy_button["state"] = DISABLED
    return Dummy_button

root = Tk()
mBar = Frame(root, relief=RAISED, borderwidth=2)
mBar.pack(fill=X)

CmdBtn = makeCommandMenu()
CasBtn = makeCascadeMenu()
ChkBtn = makeCheckbuttonMenu()
RadBtn = makeRadiobuttonMenu()
NoMenu = makeDisabledMenu()

mBar.tk_menuBar(CmdBtn, CasBtn, ChkBtn, RadBtn, NoMenu)
root.title('Menus')
root.mainloop()