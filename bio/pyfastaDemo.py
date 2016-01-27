#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyfasta import Fasta

f = Fasta('test.txt')
print f.keys()
print len(f['X80413'])
print f['X80413'][0:5]
print f.sequence({'chr':'X80413','start':0,'stop':len(f[key]),'strand':'-'},one_based=False)