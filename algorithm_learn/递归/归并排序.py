"""
核心理念:分治思想拆分问题,开辟辅助数组帮助左右两边进行排序
"""
def gb_sort(arr,L,R):
    if(L == R):
        return
    mid = L + ((R-L) >> 1)
    gb_sort(arr,L,mid) 
    gb_sort(arr,mid+1,R)
    merge(arr,L,mid,R)

def merge(arr,L,M,R): 
    tmp = []
    p1,p2 = L,M+1  # 注意merge的时候不一定是0
    # 按顺序放入辅助数组中
    while(p1<=M and p2<=R):
        if(arr[p1] < arr[p2]):
            tmp.append(arr[p1])
            p1+=1
        else:
            tmp.append(arr[p2])
            p2 +=1
    # 如果某一边有剩下的就也放在数组最后
    if(p1 <= M or p2 <= R):
        while(p1 <=M):
            tmp.append(arr[p1])
            p1 += 1
        while(p2 <= R):
            tmp.append(arr[p2])
            p2 += 1
    # 拷贝回去
    for i in range(len(tmp)):
        arr[L+i] = tmp[i]

if __name__ == "__main__":
    test = [3,1,2,5]
    gb_sort(test,0,3)
    print(test)

