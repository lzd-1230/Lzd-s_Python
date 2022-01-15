"""
算法原理:
    从头开始向后遍历(下标i),找到最小的数
    然后把最小的数和i位置交换,保证从开头开始到i是已经排好了的
    直到遍历到结尾
"""
test = [1,5,2,3,4]

# 交换数组中元素
def swap(arr,i,j):
    tmp = 0
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

# 排序流程
def select_sort(arr):
    if(len(arr) < 2):
        return
    for i in range(len(arr)):
        min_idx = i
        for j in range(i,len(arr)):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        swap(arr,min_idx,i)

print(test)