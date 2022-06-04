from tenacity import retry


grid = [list(input().split()) for _ in range(5)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

res = []
def dfs(r,c,tmp) :
    if len(tmp) == 6 :
        if not(tmp in res) :
            res.append(tmp)
        return 
    
    for d in range(4) :
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<5 and 0<=nc<5 :
            dfs(nr,nc,tmp+grid[nr][nc])
for r in range(5) :
    for c in range(5) :
        dfs(r,c,grid[r][c])
print(len(res))
