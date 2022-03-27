# -*- coding: utf-8 -*-
'''
Created on 2月-22-22 15:38
@filename: 普通二分法.py
@author: lzd
@discription: 查找值等于x的元素下标
'''
test = [1,3,4,6,7,8,9]

def binary_search(arr,target):
    l,r = 0,len(arr)-1
    while(l<=r):
        mid = (l+r) >> 1
        if(arr[mid] == target): return mid
        elif(arr[mid] < target): l = mid + 1
        else: r = mid - 1
    return -1

if __name__ == '__main__':
    print(binary_search(test,8))