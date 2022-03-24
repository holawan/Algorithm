T = int(input())



def dfs(i,j,cnt,ans): 
    global par
    if cnt >= 6 :
        result.add(ans)
        return

    else :
        for k in range(4) :
            ni = i + dr[k]
            nj = j + dc[k]
            if 0<=ni<n and 0<=nj<n :
                dfs(ni,nj,cnt+1,ans + str(grid[ni][nj]))
for t in range(1,T+1) :
    n = 4 
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    grid = [list(map(int,input().split())) for _ in range(n)]
    result = set()
    for i in range(n) :
        for j in range(n) :
            dfs(i,j,0,str(grid[i][j]))
            
    print(f'#{t} {len(result)}')
