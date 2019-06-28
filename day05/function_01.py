# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

sum = 0

def my_func(*nums):
	for num in nums:
		global sum
		sum += num
		
my_func(1, 2, 3, 4, 5)		
		
print sum
