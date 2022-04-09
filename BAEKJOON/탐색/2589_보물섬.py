from collections import deque

N,M = map(int,input().split())

grid = [list(input()) for _ in range(N)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]
res = 0
for r in range(N) :
    for c in range(M) :
        if grid[r][c] == 'L' :
            q = deque([(r,c)])
            
            visited = [[0]*M for _ in range(N)]
            visited[r][c] = 1 
            while q :
                cr,cc = q.popleft() 
                for d in range(4) :
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    if 0<=nr<N and 0<=nc<M and grid[nr][nc] == 'L' and not visited[nr][nc] :
                        visited[nr][nc] = visited[cr][cc] + 1 
                        q.append((nr,nc))
            for j in visited :
                res = max(res,max(j))
        
print(res-1)
