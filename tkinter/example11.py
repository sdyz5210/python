#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
from tkColorChooser import *
import webbrowser as web
import tkMessageBox
 
def get_tk():
    '''获取一个Tk对象'''
    return Tk()
 
def set_tk_title(tk,title):
    if title is not None and title != '':
        tk.title(title)
    else:
        tk.title('Hongten v1.0')
 
def set_tk_geometry(tk,size):
    if size is not None and size != '':
        tk.geometry(size)
    else:
        tk.geometry('670x600')
 
def get_menu(tk):
    return Menu(tk)
 
class TextViewer(Toplevel):
    """A simple text viewer dialog for IDLE
 
    """
    def __init__(self, parent, title, text, modal=True):
        """Show the given text in a scrollable window with a 'close' button
 
        """
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.geometry("=%dx%d+%d+%d" % (625, 500,
                                        parent.winfo_rootx() + 10,
                                        parent.winfo_rooty() + 10))
        #elguavas - config placeholders til config stuff completed
        self.bg = '#ffffff'
        self.fg = '#000000'
 
        self.CreateWidgets()
        self.title(title)
        self.parent = parent
        self.textView.insert(0.0, text)
  
        if modal:
            self.transient(parent)
            self.grab_set()
            self.wait_window()
 
    def CreateWidgets(self):
        frameText = Frame(self, relief=SUNKEN, height=700)
        frameButtons = Frame(self)
        self.buttonOk = Button(frameButtons, text='Close',
                               command=self.Ok, takefocus=FALSE)
        self.scrollbarView = Scrollbar(frameText, orient=VERTICAL,
                                       takefocus=FALSE, highlightthickness=0)
        self.textView = Text(frameText, wrap=WORD, highlightthickness=0,
                             fg=self.fg, bg=self.bg)
        self.scrollbarView.config(command=self.textView.yview)
        self.textView.config(yscrollcommand=self.scrollbarView.set)
        self.buttonOk.pack()
        self.scrollbarView.pack(side=RIGHT,fill=Y)
        self.textView.pack(side=LEFT,expand=TRUE,fill=BOTH)
        frameButtons.pack(side=BOTTOM,fill=X)
        frameText.pack(side=TOP,expand=TRUE,fill=BOTH)
 
    def Ok(self, event=None):
        self.destroy()
 
def view_text(parent, title, text, modal=True):
    return TextViewer(parent, title, text, modal)
 
def other():
    filename = './jack.txt'
    text = file(filename, u'r').read()
    btn1 = Button(get_tk(), text='Z-time所有域名',
                command=lambda:view_text(root, 'view_text', text))
    btn1.pack()
 
def showinfo():
    tkMessageBox.showinfo(root,u'作者 zxcbvbbbbb \n\nversion 1.0 \n\nThank you ')
     
     
 
def url1():
        web.open_new_tab('http://')
 
def url2():
        web.open_new_tab('http://')
 
def url3():
        web.open_new_tab('http://')
 
def url4():
        web.open_new_tab('http://')
 
def url5():
        web.open_new_tab('http://')
 
def url6():
        web.open_new_tab('http://')
 
def url7():
        web.open_new_tab('http://')
 
def url8():
        web.open_new_tab('http://')
 
def url9():
        web.open_new_tab('http://')
 
def url10():
        web.open_new_tab('http://')
 
def url11():
        web.open_new_tab('https://')
 
def url12():
        web.open_new_tab('http://')
 
def url13():
        web.open_new_tab('https://')
 
def url14():
        web.open_new_tab('http://')
 
def url15():
        web.open_new_tab('http://')
         
         
def popup(event):
    menubar.post(event.x_root,event.y_root)
 
def test():
    ask = askokcancel('请继续上班','你确定要这样做吗？')
    if ask:
        # to do something
        print('你选择的是：确定')
    else:
        # to do something
        print('你选择的是：取消')
 
def test2():
    ask = askquestion('Are you sure?', '你很喜欢那个女孩吗?')
    if 'yes' == ask:
        #to do something
        print('是的，我很喜欢')
    elif 'no' == ask:
        #to do something
        print('不是这样的，我不喜欢她')
 
def test3():
    '''打开文件'''
    #('All files', '*')
    openfilename = askopenfilename(filetypes=[('xml', '*.xml')])
    try:
        with open(openfilename, 'r') as fp:
            for line in fp:
                print(line)
            fp.close()
    except:
        print('Could not open File:%s'%openfilename)
 
def test4():
    '''颜色面板选择器'''
    color = askcolor(title='颜色面板')
    print color
 
def menu_url(menubar):
    '''定义菜单File'''
    filemenu=Menu(menubar,tearoff=1)
    filemenu.add_command(label='会员网',command=url1)
    filemenu.add_command(label='现金网',command=url2)
    filemenu.add_command(label='ams',command=url3)
    filemenu.add_command(label='lotto',command=url5)
    filemenu.add_command(label='bbs',command=url14)
    filemenu.add_command(label='公司邮箱',command=url4)
    filemenu.add_command(label='公司',command=url6)
    menubar.add_cascade(label='time',menu=filemenu)
    filemenu.insert_separator(6)
 
def menu_bak(menubar):
    bak_menu=Menu(menubar,tearoff=1)
    bak_menu.add_command(label='ex防御点',command=url7)
    bak_menu.add_command(label='tms防御点',command=url8)
    bak_menu.add_command(label='ams防御点',command=url15)
    menubar.add_cascade(label='防御点',menu=bak_menu)
 
def menu_domain(menubar):
    domain_menu=Menu(menubar,tearoff=1)
    domain_menu.add_command(label='godaddy',command=url9)
    domain_menu.add_command(label='dnspod',command=url11)
    domain_menu.add_command(label='hostingspeed',command=url12)
    domain_menu.add_command(label='新网',command=url10)
    domain_menu.add_command(label='邮箱管理',command=url13)
    menubar.add_cascade(label='域名管理',menu=domain_menu)
    domain_menu.insert_separator(5)
 
def menu_other(menubar):
    other_menu=Menu(menubar,tearoff=1)
    other_menu.add_command(label='在用的域名',command=other)
    other_menu.add_command(label='下班',command=test)
    other_menu.add_command(label='关于工具',command=showinfo)
    menubar.add_cascade(label='其他',menu=other_menu)
 
def init_menu_bar(menubar):
    menu_url(menubar)
    menu_bak(menubar)
    menu_domain(menubar)
    menu_other(menubar)
         
root = get_tk()
     
set_tk_geometry(root, '')
set_tk_title(root, 'Z-time运维小工具')
menubar = get_menu(root)
root.bind('<Button-3>',popup)
init_menu_bar(menubar)
root['menu'] = menubar
root.mainloop()