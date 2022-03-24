from collections import deque

dr = [0,1,0,-1]
dc=  [1,0,-1,0]

def bfs() :
    global r,c
    while que :
        s_i,s_j = que.popleft()
        for k in range(4) :
            n_i = s_i + dr[k]
            n_j = s_j + dc[k]

            if 0<=n_i<c and 0<=n_j<r and grid[n_i][n_j] == 0 and not visited[n_i][n_j] :
                visited[n_i][n_j] = visited[s_i][s_j] + 1
                que.append([n_i,n_j])

r,c = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(c)]
visited = [[0]*r for _ in range(c)]

que = deque()
for i in range(c) :
    for j in range(r) :
        if grid[i][j] ==1 :
            que.append([i,j])
            visited[i][j] = 1




bfs()
grid_sum = 0 
for i in grid :
    grid_sum += sum(i)

second = 0
for i in range(c) :
    for j in range(r) :
        if visited[i][j] == 0 and grid[i][j] == 0 :
            second = 1 
            break

if grid_sum == r*c :
    print(0)
elif second :
    print(-1)
else :
    my_max = 0 
    for i in visited :
        my_max = max(my_max,max(i))
    print(my_max-1)