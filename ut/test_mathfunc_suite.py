#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.*

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
	suite = unittest.TestSuite()
	tests = [TestMathFunc("test_add"),TestMathFunc("test_minus"),TestMathFunc("test_divide"),TestMathFunc("test_multi")]
	suite.addTests(tests)
	with open("testreport.txt","a") as f:
		runner = unittest.TextTestRunner(stream=f,verbosity=2)
		runner.run(suite)