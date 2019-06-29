# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

F = open("data/unsort.txt", "r")

A = []

i = 0

while i < 10:
	num = F.readline()
	A.append(num)  
	i += 1
  
A = sorted(A)
  
print(A)
  
F.close()
