#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
randlist = []
lst = []
for i in range(3):
    n = random.randint(-10, 30)
    randlist.append(n)
print(randlist)
positive = 0
for i in range(len(randList)):
    if randList[i] > 0:
        positive += randList[i]
print(positive)
for i in range(positive[1], positive[-1]):
    lst += positive
print(lst)
