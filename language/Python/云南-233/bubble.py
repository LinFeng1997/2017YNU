# -*- coding: utf-8 -*-
# 生成随机数 #
I=[]
s=1
from random import randint
while s<10001:
    a=randint(1,10000)
    print a
    s=s+1
    I.append(a)
# 定义冒泡排序函数 #  
def bubble(List):
    for j in range(len(List)-1,0,-1):
        flag = True
        for i in range(0, j):
            if List[i] > List[i+1]:
                flag = False
                List[i], List[i+1] = List[i+1], List[i]
        if flag:
            return List
    return List
# 排序 #
s=bubble(I)
result=str(s)
print result
f=file('f.txt','w')
f.write(result)
f.close()
# 计时 #
import time  
starttime = time.time()
print 'start:%f' % starttime
for i in range(10):
    print i
endtime = time.time()  
print 'end:%f' % endtime
print 'total time:%f' % (endtime-starttime) 
