# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class phoneBook(object):
  def __init__(self, name, number, religion, photo):
		self.name = name
		self.number = number
		self.religion = religion
		self.photo = photo
  print "info is saved"
    
  def showData(self):
  	print("이름 : {}\n번호 : {}\n사는 곳 : {}\n사진 : {}\n".format(self.name, self.number, self.religion, self.photo))  
		
class Best_Friend(phoneBook):
	def add(self, age, sex, story):
		self.age = age
		self.sex = sex
		self.story = story
		self.count = 0
    
	def count(self):
		self.count += 1
		
	def printcount(self):
		print("연락횟수 : %s\n" % self.count)
