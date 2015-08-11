#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

from bottle import route, run, template

@route('/hello')
def index():
	return "Hello Bottle"

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
