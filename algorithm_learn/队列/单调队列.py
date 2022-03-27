# -*- coding: utf-8 -*-
'''
Created on 2月-22-22 10:37
@filename: 单调队列.py
@author: lzd
@discription: 单调队列的基础用法: 维护区间最值
'''
test = [3,1,5,7,9,1,5]
head = tail = 0
q = [None for i in range(len(test))] # 一般存储数组下标

if __name__ == '__main__':
    # 构造一个2的窗口进行扫描,得到实时区间的最小值
    win = 2
    q[tail] = 0; tail += 1 # 区间内默认加入第一个元素
    for i in range(1,len(test)):
        # 回退到满足单调性的地方
        while(tail-head and test[q[tail-1]] >= test[i]):
            tail -= 1
        q[tail] = i; tail += 1
        if(q[head] < i-win+1):
            head += 1
        print(q[head])
