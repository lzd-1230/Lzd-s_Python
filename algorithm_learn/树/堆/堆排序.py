# -*- coding: utf-8 -*-
'''
Created on 2月-20-22 23:22
@filename: 堆排序.py
@author: lzd
@discription: 实现从小到大的排序
'''

class Heap_Sort():
    def __init__(self,data) -> None:
        self.data = data # 下标从1开始的数组
        
    def down_adjust(self,i,n):
        """
        i:从第i个位置开始向下调整
        n:数组的最后一个元素的下标
        """
        idx = i
        while(idx<<1 <= n):
            # 比较和两个孩子的大小
            tmp = idx
            left,right = idx<<1, idx<<1 | 1
            if(self.data[tmp] < self.data[left]): tmp = left
            if(right<=n and self.data[tmp]<self.data[right]): tmp = right
            if(tmp == idx): break
            self.data[tmp],self.data[idx] = self.data[idx],self.data[tmp]
            idx = tmp

    def build_heap(self):
        n = len(self.data) - 1 # 最大的下标
        # 向下调整(线性建堆)
        for i in range(n>>1,0,-1):  # 从倒数第二层开始调整
            self.down_adjust(i,n)
        # n次弹出
        for i in range(n,1,-1):
            self.data[1], self.data[i] = self.data[i], self.data[1]
            self.down_adjust(1,i-1) # 还剩i-1个元素,要从堆顶开始向下调整
            
if __name__ == '__main__':
    arr = [None,4,1,2,3,5]
    h = Heap_Sort(arr)
    h.build_heap()
    print(h.data)