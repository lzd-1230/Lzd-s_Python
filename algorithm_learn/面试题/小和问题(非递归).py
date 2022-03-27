"""
将每一个数左边比它小(排序)的数累加起来(归并)
"""
# 非递归版本
arr = [3,1,2,4]
def small_sum(arr):
    step = 1
    res = 0
    while(step <= len(arr)):
        L = 0
        # 在当前步长下逐渐往后合并
        for i in range(0,len(arr),step):
            M = L+step-1
            if(M >= len(arr)):
                break
            R = min(M+step,len(arr)-1)
            res += merge(arr,L,R,M)
            L = R+1
        step *= 2
    return res

def merge(arr,L,R,M):
    p1,p2 = L,M+1
    res = 0
    tmp = []
    while(p1<=M and p2 <= R):
        if(arr[p1]<arr[p2]):
            res += (R-p2+1)*arr[p1] # 在这一轮合并中有多少个大的
            tmp.append(arr[p1])
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1
    while(p1 <= M):
        tmp.append(arr[p1])
        p1 += 1
    while(p2 <= M):
        tmp.append(p2)
        p2 += 1
    for idx,ele in enumerate(tmp):
        arr[idx+L] = ele
    return res

if __name__ == "__main__":
    res = small_sum(arr)
    print(res)
    print(arr)
