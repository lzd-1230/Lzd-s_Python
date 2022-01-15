"""
算法原理:
    从i位置开始向后,保证i前面的数都已经排好
    那么每次只需要比较i和i之前的数的大小
        如果[i]比[i-1]小,则交换
            再比较[i-1]和[i-2]
                ...
        一旦中间有一次不用交换,就可以停下来
"""
test = [1,5,2,3,4]

# 交换数组中元素
def swap(arr,i,j):
    tmp = 0
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

# 排序流程
def insert_sort(arr):
    if(len(arr) < 2):
        return
    for i in range(len(arr)):
        for j in range(i-1,0,-1):
            if(j>0 and arr[j]>arr[j+1]):
                swap(arr,j,j+1)

insert_sort(test)

print(test)