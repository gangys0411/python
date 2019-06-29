# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Member:
	
	def setId(self, id, password):
		self.id = id
		self.password = password
				
	def getId(self):
		print(self.id)
		print(self.password)
		
Member1 = Member()
Member2 = Member()

Member1.setId(1, 1234)
Member2.setId(2, 5678)

Member1.getId()
Member2.getId()
