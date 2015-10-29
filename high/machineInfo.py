#!/usr/bin/python
# -*- coding: utf-8 -*-

import psutil

print psutil.cpu_count()

print psutil.cpu_count(logical=False)

print psutil.virtual_memory()

(total,available,percent,used,free,active,inactive,wired)=  psutil.virtual_memory()

print total

print total/1000000000