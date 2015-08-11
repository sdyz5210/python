#!/usr/bin/python
# -*- coding: utf-8 -*-


def first_case():
    print "first"

def second_case():
    print "second"

def third_case():
    print "third"

mycase = {
'first': first_case, #do not use ()
'second': second_case, #do not use ()
'third': third_case #do not use ()
}
myfunc = mycase['first']
myfunc()