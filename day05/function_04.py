# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def opr_func(a, b):
	opr = [a + b, a - b, a * b]
	return opr

a = input()
b = input()

print(opr_func(a, b))
