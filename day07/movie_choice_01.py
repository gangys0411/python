# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


movies = ["Batman", "Harry Porter", "Scream", "Happy Dog"]


#for 문을 이용하여 movies 안에 있는 영화 제목을 모두 출력합니다.
print "영화 목록 : "
for movie in movies:
	print("%s " % movie)

# 사용자에게 어떤 영화를 볼지 질문을 출력합니다.
print "관람할 영화를 선택해 주세요"
choice = raw_input()


#while 문을 이용하여 선택한 영화가 목록에 없을 시에는 영화 제목을 다시 입력받습니다.
while choice not in movies:
	print "다시 선택해 주세요."
	choice = raw_input()
