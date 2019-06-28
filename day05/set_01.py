# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

S1 = {1, 3, 5, 7}
S2 = {5, 6, 7, 8, 9}

print(S1 & S2)
print(S1 | S2)
print(S1 - S2)

S1.add("강영석")

print(S1)

S2.update(["리스트", 1])

print(S2)

S2.remove(9)

print(S2)
