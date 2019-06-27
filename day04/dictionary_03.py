# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

animals = {'cat' : 1, 'dog' : 10, 'horse': 3}
# 모든 key를 반환하여 keys 에 저장

keys = animals.keys()
print keys

# 모든 value를 반환하여 values에 저장

values = animals.values()
print values

# animals 의 모든 쌍 삭제

animals.clear()

# animals 내에 'cat' 이라는 키가 있는지 확인

print("cat" in animals)
