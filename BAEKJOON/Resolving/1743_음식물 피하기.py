import sys 

sys.setrecursionlimit(10000)

N,M,K = map(int,input().split())

dr = [1,0,-1,0]
dc = [0,1,0,-1]
res = 0
def dfs(r,c) :
    global cnt 
    cnt += 1 

    for d in range(4) :
        nr =r + dr[d]
        nc =c+ dc[d]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and grid[nr][nc] :
            visited[nr][nc] = 1
            dfs(nr,nc)

grid = [[0]*M for _ in range(N)]

for _ in range(K) :
    r,c = map(int,input().split())
    grid[r-1][c-1] = 1 

visited = [[0]*M for _ in range(N)]

for r in range(N) :
    for c in range(M) :
        if not visited[r][c] and grid[r][c] :
            visited[r][c] = 1
            cnt = 0
            dfs(r,c)
            res = max(res,cnt)

        
print(res)
