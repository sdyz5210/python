#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

#注意把password设置成数据库root的口令
conn = mysql.connector.connect(user='root',password='novacloud',database='test',use_unicode=True)

cursor = conn.cursor()

#创建user表
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user(id,name) values(%s,%s)',['1','Jack'])
cursor.rowcount
conn.commit()
cursor.close()

#运行查询
cursor = conn.cursor()

cursor.execute('select * from user where id=%s',['1'])
#cursor.execute('select * from user where id=%s' %'1')

values = cursor.fetchall()

print '打印数据库查询结果',values

cursor.close()
conn.close()
