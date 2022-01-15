"""
一个数组有一种数出现了k次,其他数都出现了m次,其中m>k,m>1求出现了k次的那个数
    !!!!等弄懂了hashmap后来补一个对数器
"""
from os import replace
from random import random
import sys
import numpy as np

# print(sys.getsizeof(3)) # python中长整型一般占用28位

test = [3,3,3,4,4,4,10,10]
m = 3
n = 2
# 将十进制转换成二进制的列表
def return_bin(num):
    res = []
    for i in range(28):
        res.insert(0,(num >> i) & 1) # 一直在开头插入
    return res

# 将二进制列表转换回10进制的数
def return_oct(arr:list):
    res = 0
    arr.reverse() # 注意这里要
    for idx,ele in enumerate(arr):
        res += (2**idx)*ele
    return res

def sovlement():
    record = [0 for i in range(28)]
    # 将每一个
    for ele in test:
        tmp = return_bin(ele)
        # 将两个数组对应元素相加
        record = np.sum([record,tmp], axis=0)

    res = [0 if ele % m==0 else 1 for ele in record]
    print(return_oct(res))

sovlement()
