#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abifpy import Trace

yummy = Trace('/Users/mac/Documents/data/ab1/HBV_B.ab1')

print yummy.seq

print yummy.qual

print yummy.qual_val

print yummy.id

print yummy.name