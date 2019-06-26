# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = "Contrary to popular belief, Lorem Ipsum is not simply random text."

# 't' 의 개수 출력

print(a.count("t"))

# 가장 먼저 나오는 'i' 의 인덱스 출력

print(a.index("i"))

# 모두 대문자로 바꾼 뒤 출력

print(a.upper())

# 모두 소문자로 바꾼 뒤 출력

print(a.lower())

# 'a' 를 'b'로 바꾼 뒤 출력

print(a.replace("a", "b"))

# 문자열을 공백(" ")으로 나눈 것을 출력

print(a.split(" "))
