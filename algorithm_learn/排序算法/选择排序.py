"""
不稳定排序
    为什么选择排序是不稳定的?
    答:因为每次交换的对象是非稳定的第一位
       也就是非稳定区的相对顺序可能会被打乱

算法原理:
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
    # 待排序区的开头
    for i in range(len(arr)):
        min_idx = i
        # 遍历待排序区的所有元素找最小值
        for j in range(i,len(arr)):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        swap(arr,min_idx,i)

print(test)