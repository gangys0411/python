# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Person:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def aboutMe(self):
		print "나는 부모 클래스 입니다."
		
		
class Student(Person):
	school = "goorm school"
	
	def aboutMe(self):
		print("이름 : {} 나이 : {}".format(self.name, self.age))
		
Student1 = Student("홍길동", 19)
Student1.aboutMe()
