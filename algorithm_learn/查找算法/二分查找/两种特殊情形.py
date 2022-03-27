# -*- coding: utf-8 -*-
'''
Created on 2月-22-22 15:44
@author: lzd
@discription: 二分查找中两种特殊情形
口诀:找第一个则r指针小心翼翼,找最后一个,那么l指针小心翼翼
'''

# 11111000000 中找到最后一个1
def binary_search1(arr,last_tar):
    l,r = 0,len(arr) - 1
    while(l<r):
        mid = (l+r+1)>>1 # 这里是让mid=r的时候还可以继续更新
        if(arr[mid] == last_tar): l = mid # 左指针是最后返回的值
        elif(arr[mid] < last_tar): r = mid-1
        else: l = mid + 1
        # print(f"l:{l} r:{r} mid:{mid}")
    return l if arr[l] == last_tar else -1

# 000000111 中找到第一个1
def binary_search2(arr,first_tar):
    l,r = 0,len(arr) - 1
    while(l<r):
        mid = (l+r)>>1 # 最后mid=l的时候还会更新
        if(arr[mid] == first_tar): r = mid
        elif(arr[mid] < first_tar):
            l = mid +1
        else: r = mid - 1
        print(f"l:{l} r:{r} mid:{mid}")
    # 这里最后r=l的时候随意返回一个就行
    return r if arr[r] == first_tar else -1
 
if __name__ == '__main__':
    arr1 = [2,2,2,2,2,2,2,2,1,1,1,0,0,0]
    arr2 = [0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2]
    print(binary_search1(arr1,1))
    print(binary_search2(arr2,1))
