
# -*- coding: utf-8 -*-
'''
Created on 2月-22-22 13:20
@filename: 冒泡.py
@author: lzd
@discription: 冒泡排序(稳定)
'''
test = [5,3,1,2,5,6]

if __name__ == '__main__':
    for i in range(len(test)-1,0,-1): # 已排序的边界
        for j in range(0,i): # 0-i-1的位置冒泡
            if(test[j] > test[j+1]):
                test[j],test[j+1] = test[j+1],test[j]
                chang = True
        # 如果某一次冒泡了一遍居然没有变化,那就说明已经可以结束了
        if(chang == True):
            chang = False
        else:
            break
        
    print(test)

