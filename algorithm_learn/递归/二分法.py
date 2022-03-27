"""
递归求数组在[L,R]上的最小值
"""
arr = [5,6,7,2]

# 任何递归一定可以写成迭代行为
def find_max(L:int,R:int,arr:list):
    mid = (L + ((R-L)>>2))
    if(L == R):
        return arr[R]
    else:
        # 不能用mid-1去做,可能会出现左边界比右边界小的情况
        return max(find_max(L,mid,arr),find_max(mid+1,R,arr))
    

if __name__ == "__main__":
    print(find_max(0,3,arr))