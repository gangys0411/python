# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Customer:
	welcome = "반갑습니다"
	
	def info(self, id):
		print(id)

ins_Customer = Customer()

print(ins_Customer.welcome)
ins_Customer.info(1)
