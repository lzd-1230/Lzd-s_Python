arr = [0,0,0,1,1,1,1,1]

def binary_search2(arr,first_tar):
    l,r = 0,len(arr) - 1
    while(l<r):
        mid = (l+r)>>1 # 最后mid=l的时候还会更新
        if(arr[mid] == first_tar): r = mid
        elif(arr[mid] < first_tar):
            l = mid +1
        else: r = mid - 1
        print(f"l:{l} r:{r} mid:{mid}")
    # 这里最后r=l的时候随意返回一个就行
    return r if arr[r] == first_tar else -1

print(binary_search2(arr,1))