n,m = map(int,input().split())

grid = list(list(map(int,input().split())) for _ in range(n))
max_val = max(map(max, grid))


dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r,c,cnt,S) :
    global a 

    if a >= S + max_val * (4-cnt) :
        return 
    if cnt >=4 :
        if S>a :
            a = S
        return
    
    for d in range(4) :
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<n and 0<=nc<m and not visited[nr][nc] :
            visited[nr][nc] = 1
            dfs(nr,nc,cnt+1,S+grid[nr][nc])
            visited[nr][nc] = 0 

def cross(r,c,S) :
    global a 
    tmp = []
    for d in range(4) :
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<n and 0<=nc<m :
            S += grid[nr][nc]
            tmp.append(grid[nr][nc])
    if len(tmp) == 3 :
        if S > a :
            a = S
    if len(tmp) == 4 : 
        for t in tmp :
            if S - t >a :
                a = S  - t

a = 0
visited = [[0]*m for _ in range(n)]
for r in range(n) :
    for c in range(m) :
        visited[r][c] = 1 
        dfs(r,c,1,grid[r][c])
        visited[r][c] = 0
        cross(r,c,grid[r][c])

print(a)