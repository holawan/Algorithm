from collections import deque

n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

wall = []
virus = []
road  = []

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for i in range(n) :
    for j in range(m) :
        if grid[i][j] == 0 :
            road.append((i,j))
        elif grid[i][j] == 1 :
            wall.append((i,j))
        else :
            virus.append((i,j))

sub_wall = []

l = len(road)

for i in range(l-2) :
    for j in range(i+1,l-1) :
        for k in range(j+1,l) :
            sub_wall.append((road[i],road[j],road[k]))


ans = 0 

for w in sub_wall :
    for _ in range(3) :
        grid[w[_][0]][w[_][1]] = 1 
    visited = set()
    q = deque(virus[:])
    while q :
        cr,cc = q.popleft()
        visited.add((cr,cc))
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0<=nr<n and 0<=nc<m and not (nr,nc) in visited and  grid[nr][nc] ==0: 
                q.append((nr,nc))

    v = len(visited)
    tmp_res = n*m - len(wall) - v -3 
    if tmp_res > ans :
        ans = tmp_res
    for _ in range(3) :
        grid[w[_][0]][w[_][1]] = 0
                
print(ans)

        
    