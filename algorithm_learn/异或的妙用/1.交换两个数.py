"""
①交换两个数(不需要额外变量),但是其实速度上甚至更慢...这个装逼用的...
"""
# ****************1***************
from random import random
import timeit
def swap1(a,b):
    b = a^b 
    a = a^b
    b = a^b

def swap2(a,b):
    tmp = a
    a = b
    b = tmp

# a,b= 1,3
# t1 = timeit.Timer("swap1(a,b)","from __main__ import swap1,a,b")
# print(t1.timeit(number=10000000))
# t2 = timeit.Timer("swap2(a,b)","from __main__ import swap2,a,b") 
# print(t2.timeit(number=10000000))
# ****************1***************


