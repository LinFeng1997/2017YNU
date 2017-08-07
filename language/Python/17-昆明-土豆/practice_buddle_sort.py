#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from random import sample as radsmp

L1 = []
Source_List = list(range(1,1000000))
L1 = radsmp(Source_List, 10000)
print("List Length:", len(L1))
t1 = time.time()
for i in range(len(L1)-1, 0, -1):
    for j in range(0, i):
        if L1[j] > L1[j + 1]:
            # dbgvar1 = L1[j]
            # dbgvar2 = L1[j + 1]
            # print("before:",dbgvar1,dbgvar2,"\n")
            # time.sleep(2)
            L1[j], L1[j + 1] = L1[j + 1], L1[j]
            # dbgvar1 = L1[j]
            # dbgvar2 = L1[j + 1]
            # print("after:",dbgvar1,dbgvar2,"\n")
            # time.sleep(2)
        else:
            pass
print('Sorted List:', L1)
t2 = time.time()
print("Time usage:", t2 - t1 , "seconds")
