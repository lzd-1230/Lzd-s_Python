"""
稳定
迭代版本:利用步长的概念来完成二分的效果
    可以更清晰地看到O(N)*logN的原理
"""
arr = [4,1,-1,4,6,8,10]

def gb_sort(arr):
    step = 1
    while(step <= len(arr)):
        L = 0 # 每一次决定好step后都从头开始
        for i in range(0,len(arr),step):
            M = L+step-1
            # 左数组都已经超过了就不用排了
            if(M >= len(arr)):
                break
            R = min(len(arr)-1,M+step)
            merge(arr,L,R,M)
            # merge完一次之后向后挪
            L = R + 1
        step *= 2

def merge(arr,L,R,M):
    p1,p2 = L,M+1
    tmp = []
    while(p1<=M and p2<=R):
        if(arr[p1]<arr[p2]):
            tmp.append(arr[p1])
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1
    while(p1<=M):
        tmp.append(arr[p1])
        p1+=1
    while(p2<=R):
        tmp.append(arr[p2])
        p2+=1
    for idx,ele in enumerate(tmp):
        arr[idx+L] = ele

if __name__ == "__main__":
    gb_sort(arr)
    print(arr)

