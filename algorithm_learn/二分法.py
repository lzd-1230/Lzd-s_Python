"""
二分法的用处:
    构造排他性,一半边肯定没有,之后再进行构造终点和排他就可以了

1.在有序序列中查找>=n的最左边的那一个的下标
2.查找无序数组中局部极小值()
"""
# 1.
test = [1,2,2,3,4]
def find_leftmin_idx(arr,n):
    L,R = 0,len(arr)-1
    i=0
    if(len(arr) < 2):
        return None

    while(L < R):           # 列表中至少还有两个数

        mid = int(L + ((R-L) >> 1))
        if(arr[mid] >= n):
            R = mid - 1 
        elif(arr[mid] < n):
            L = mid + 1 
        i+=1
        print(f"第{i}轮 L={L} R={R} m={mid}")
    return L

# 2.
test = [10,1,2,3,4,2,5,3,10]
def find_minpoint_inx(arr):
    if(arr[0]<arr[1]):
        return 0
    if(arr[-1]< arr[-2]):
        return len(arr) -1 
    L,R = 1,len(arr) - 2
    i = 0
    # 在这里的时候肯定可以确定中间有极小值
    while(L<R):
        mid = L+((R-L)>>1)
        print(f"第{i}轮 L={L} R={R} m={mid}")
        if(arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]):
            return mid
        elif(arr[mid] > arr[mid-1]):
            R = mid - 1
        elif(arr[mid] > arr[mid+1]):
            L = mid + 1
        i+=1
    return L

if __name__ == "__main__":
    # print(f"结果下标:{find_leftmin_idx(test,2)}") # 1
    # print(f"结果{find_minpoint_inx(test)}")


