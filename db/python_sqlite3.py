#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print cursor.rowcount
cursor.close()
conn.commit()
conn.close()