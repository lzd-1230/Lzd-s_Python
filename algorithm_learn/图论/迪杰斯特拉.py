NUM = 9

# 1.邻接矩阵
g = [[float('inf') for i in range(NUM)] for i in range(NUM)]  
g[0][1]=4;g[0][7]=8;g[1][7]=3;g[1][2]=8;g[7][8]=1;g[7][6]=6;g[2][8]=2;g[8][6]=6;g[2][3]=7;g[2][5]=4;g[6][5]=2;g[5][3]=14;g[3][4]=9;g[5][4]=10
for i in range(NUM):
    for j in range(NUM):
        if(g[i][j]!=float('inf')):
            g[j][i] = g[i][j]

# 2.找到最短路径
visited = [False for i in range(NUM)]
dis = [float('inf') for i in range(NUM)]
parent = [-1 for i in range(NUM)]

start = cur = 0
dis[start] = 0

while(True):
    # 先根据当前节点更新dis
    visited[cur] = True
    for i in range(NUM):
        # 找到了更短的路径
        if(g[cur][i] + dis[cur] < dis[i]):
            dis[i] = g[cur][i]+dis[cur]
    # 局部最小?
    tmp = float('inf')
    for i in range(NUM):
        if(not visited[i] and dis[i] < tmp):
            min_idx = i
            tmp = dis[i]    
    parent[min_idx] = cur
    cur = min_idx
    if(all(visited)):
        break

print(dis[4])