from collections import deque
import copy
dr = [0,1,0,-1]
dc = [1,0,-1,0]
n = int(input())


def bfs() :
    global mark
    while que :
        s_i,s_j = que.popleft()
        grid[s_i][s_j] = 0
        mark_grid[s_i][s_j] = mark 
        for k in range(4) :
            n_i = s_i +dr[k]
            n_j = s_j +dc[k]
            if 0<= n_i<n and 0<=n_j<n and grid[n_i][n_j] :
                que.append([n_i,n_j])

grid= [list(map(int,input())) for _ in range(n)]
mark_grid = copy.deepcopy(grid)
mark = 1
ans = [0]*626 
for i in range(n) :
    for j in range(n) :
        if grid[i][j] :
            que = deque()
            que.append([i,j]) 
            bfs()
            mark += 1

for i in range(n) :
    for j in range(n) :
        ans[mark_grid[i][j]] += 1

ans = sorted(ans[1:mark])

result = str(mark-1)+'\n'

for i in ans :
    result += str(i) +'\n'
print(result)
