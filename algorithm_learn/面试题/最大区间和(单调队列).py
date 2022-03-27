"""
核心点:
    1.区间和问题->用前缀和简化后思考
    2.维护区间极值需要使用单调队列(0位置的特殊性)

"""
arr = input()
arr_t = input()
n,m = list(map(int,arr.strip().split(" ")))
arr = list(map(int,arr_t.strip().split(" ")))
arr.insert(0,0)
que = [0 for i in range(n)] # 提前构造特定长度的数组
head,tail = 0,0
ans = 0

# 拿到前序和
be_sum = [0]  # s[0]为0有特殊含义

for i in range(1,n+1):
    be_sum.append(arr[i]+be_sum[i-1])
##    print(be_sum)
que[tail] = 0; tail+=1 # 0的特殊含义

for i in range(1,n+1):
    # 判断是否能够更新答案
    ans = max(ans,be_sum[i]-be_sum[que[head]])
    while(tail-head and be_sum[que[tail-1]] >= be_sum[i]):
        tail -= 1
    que[tail] = i; tail+=1
    # 判断队头是否过期
    if(que[head] < i-m+1):
        head+=1
print(ans)

     
        
