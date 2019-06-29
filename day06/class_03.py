# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Member:
	
	def __init__(self, id, password):
		self.id = id
		self.password = password
		
	def getId(self):
		print(self.id)
		print(self.password)
		
Member1 = Member(1, 1234)
Member1.getId()
