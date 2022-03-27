# -*- coding: utf-8 -*-
'''
Created on 2月-22-22 14:24
@filename: 快速排序.py
@author: lzd
@discription: 快速排序
'''
 
test = [3,1,2,3,5]


def quick_sort(arr,l,r):
    if(r<=l): return
    x,y,z = l,r,arr[l] # 选取基准值
    while(x<y):
        # 右指针缩
        while(x<y and arr[y]>z): y-=1
        if(x<y): arr[x] = arr[y]; x+=1
        # 左指针缩
        while(x<y and arr[x]<z): x+=1
        if(x<y): arr[y] = arr[x]; y-=1
    arr[x] = z
    quick_sort(arr,l,x-1)
    quick_sort(arr,x+1,r)


if __name__ == '__main__':
    quick_sort(test,0,len(test)-1)
    print(test)