# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

my_list = [1, 2, 3, 4, 5]
my_list = sorted(my_list)
F = open("data/out.txt", "w")
  
#파일에 써보세요!

for i in my_list:
	data = "%d\n" % i
	F.write(data)
  
F.close()
