#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time

L1 = [i for i in range(1000000)]
print("List Length:", len(L1))
t1 = time.time()
for j in range(0, len(L1) - 1):
    if L1[j] > L1[j + 1]:
        L1[j], L1[j + 1] = L1[j + 1], L1[j]
    else:
        pass
print('Sorted List:', L1)
t2 = time.time()
print("Time usage:", t2 - t1)
