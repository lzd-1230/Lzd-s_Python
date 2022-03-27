"""
稳定
"""
test = [9,5,2,3,4]

# 排序流程
def insert_sort(arr):
    if(len(arr) < 2):
        return
    # 外层是稳定区
    for i in range(len(arr)): # [0,last] i作为待排序区的开头,每次就是i往前插队
        for j in range(i-1,-1,-1):  # j=i-1就是已排序区的结尾,就是插队者第一个要比较的对象
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

insert_sort(test)
print(test)