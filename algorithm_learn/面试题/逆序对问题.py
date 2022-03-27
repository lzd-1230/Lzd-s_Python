"""
逆序对问题:某一位右边有多少个比它小的数
"""
arr = [8,4,5,7,1,3,6,2]

def gb_sort(arr,L,R):
    if(L == R):
        return

    M = L+ ((R-L) >> 1)
    gb_sort(arr,L,M)
    gb_sort(arr,M+1,R)
    merge(arr,L,M,R)


def merge(arr,L,M,R):
    p1,p2 = L,M+1
    tmp = []
    while(p1<=M and p2<=R):
        if(arr[p1] > arr[p2]):
            tmp.append(arr[p1])
            # 在归并排序中把右边的给打印出来即可
            for i in range(p2,R+1):
                print(arr[p1],arr[i])
            p1+=1
        else:
            tmp.append(arr[p2])
            p2 += 1
    while(p1<=M):
        tmp.append(arr[p1])
        p1 += 1
    while(p2 <= R):
        tmp.append(arr[p2])
        p2 += 1
    # 归并排序的重点!
    for i in range(len(tmp)):
        arr[L+i] = tmp[i]

if __name__ == "__main__":
    gb_sort(arr,0,len(arr)-1)
    