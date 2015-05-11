#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#filename: sumdict.py

from collections import Counter

map1 = {'chr1':1,'chr2':1,'chr3':1,'chr4':1}
map2 = {'chr2':1,'chr5':1,'chr3':1,'chr4':1}
map3 = {'chr7':1,'chr6':1,'chr3':1,'chr4':1}

print Counter(map2)+Counter(map1)+Counter(map3)

l = [['chr1',1,50,200],['chr1',1,50,20],['chr2',1,50,200],['chr1',2,50,200]]

for i,j,k,h in l:
	print i,j,k,h