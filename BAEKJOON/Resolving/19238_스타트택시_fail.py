from collections import deque


N,M,E = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

sr,sc = map(int,input().split())
sr -=1 ;sc-=1
guests = [list(map(int,input().split())) for _ in range(M)]

res = 0
INF = int(10e9)
for r in range(N) :
    for c in range(N) :
        if grid[r][c] :
            grid[r][c] = INF
i = 1 
for guest in guests :
    grid[guest[0]-1][guest[1]-1] = i
    grid[guest[2]-1][guest[3]-1] = -i
    i += 1 

q = deque([[sr,sc,E]])

dr = [1,0,-1,0]
dc = [0,1,0,-1]

riding = []

charge = 0
visited = [[0]*N for _ in range(N)]
visited[sr][sc] = 1 

while q :
    r,c,e = q.popleft()
    print(q)
    if M == 0 :
        res = e 
        break
    if e<=0 :
        res = 0
        break 
    for d in range(4) :
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and grid[nr][nc] != INF:
            if grid[nr][nc] == 0 :
                q.append((nr,nc,e-1))
                visited[nr][nc] = visited[r][c] + 1

            elif grid[nr][nc] >0 :
                if riding :
                    q.append((nr,nc,e-1))
                    visited[nr][nc] = visited[r][c] + 1
                else :
                    q.clear()
                    sr,sc = nr,nc 
                    now = grid[nr][nc]
                    q.append((sr,sc,e-1))
                    visited = [[0]*N for _ in range(N)]
                    visited[sr][sc] = 1 
                    riding.append(1)
                    break
            else :
                if riding and grid[nr][nc] == -now :
                    riding = []
                    q.clear()
                    grid[sr][sc] = 0
                    sr,sc = nr,nc
                    q.append([nr,nc,(e-1)+(visited[r][c]*2)])
                    visited = [[0]*N for _ in range(N)]
                    visited[sr][sc] = 1
                    M -= 1 
                    grid[nr][nc] = 0
                    break
                else :
                    q.append((nr,nc,e-1))
                    visited[nr][nc] = visited[r][c] + 1 
print(res-1)