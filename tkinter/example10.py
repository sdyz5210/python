#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
from tkColorChooser import *
import webbrowser as web
 
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
        web.open_new_tab('')
 
def url10():
        web.open_new_tab('')
 
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
    ask = askokcancel('askokcancel messagebox','你确定要这样做吗？')
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
    filemenu.add_command(label='智世代',command=url6)
    menubar.add_cascade(label='Z-time',menu=filemenu)
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
 
def init_menu_bar(menubar):
    menu_url(menubar)
    menu_bak(menubar)
    menu_domain(menubar)
         
root = get_tk()
set_tk_geometry(root, '')
set_tk_title(root, 'Z-time运维小工具')
menubar = get_menu(root)
root.bind('<Button-3>',popup)
init_menu_bar(menubar)
root['menu'] = menubar
root.mainloop()