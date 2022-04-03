from collections import deque
import itertools
n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

empty = []
walls = []
virus = []

for i in range(n) :
    for j in range(m) :
        if grid[i][j] == 0 :
            empty.append((i,j))
        elif grid[i][j] == 1 :
            walls.append((i,j))
        elif grid[i][j] == 2 :
            virus.append((i,j))



dx = [0,1,0,-1]
dy = [1,0,-1,0]

tmp_walls =list(itertools.combinations(empty,3))

res = 0
for candidate_wall in tmp_walls :

    for i,j in candidate_wall :
        grid[i][j]= 1 


    q = deque(virus)

    visited= set()

    while q :
        x,y, = q.popleft()
        visited.add((x,y))
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited and grid[nx][ny] == 0 :
                
                q.append((nx,ny))

    infected = len(visited)

    tmp_res = n*m - len(walls) - infected - 3

    if res<tmp_res :
        res = tmp_res

    for i,j in candidate_wall :
        grid[i][j] = 0

print(res)