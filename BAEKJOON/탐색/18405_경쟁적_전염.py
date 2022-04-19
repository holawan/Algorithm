from collections import deque


N,K = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

lst = []
visited = [[0]*N for _ in range(N)]
for r in range(N) :
    for c in range(N) :
        if grid[r][c] :
            #좌표와 바이러스 번호 넣어주기 
            lst.append([r,c,grid[r][c]])
            #방문처리 
            visited[r][c] = 1 

#바이러스 번호 순 정렬 
lst.sort(key = lambda x:x[2])


dr = [1,0,-1,0]
dc = [0,1,0,-1]

#큐에 넣기 
q = deque(lst)
result = 0
while q :

    cr,cc,v = q.popleft()
    if visited[cc][cr] > S :
        break 

    for d in range(4) :
        nr = cr + dr[d]
        nc = cc + dc[d]

        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] :
            grid[nr][nc] = v
            visited[nr][nc] = visited[cr][cc] + 1 
            q.append([nr,nc,v])
    if grid[X-1][Y-1] :
        result = grid[X-1][Y-1]
        break 

print(result)
