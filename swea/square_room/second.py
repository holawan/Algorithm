from collections import deque
T = int(input())

for t in range(1,T+1) : 
    n = int(input())
    grid = [list(map(int,input().split())) for _ in range(n)]

    dr = [0,-1,0,1]
    dc = [1,0,-1,0]

    visited = [[0]*n for _ in range(n)]
    def func(i,j) :
        global tmp_max 
        q = deque([i,j])
        visited[i][j] = 1
        tmp_max+=1  
        while q :
            ci,cj = q.popleft()
            for k in range(4) :
                ni ,nj = ci+dr[k],cj+dc[k] 
                if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and abs(grid[ci][cj]-grid[ni][nj])==1 :
                    q.append((ni,nj))
                    visited[ni][nj] = 1 
                    tmp_max +=1 
    my_max = 0
    idx = 100
    for i in range(n) :
        for j in range(n) :
            tmp_max = 0
            func(i,j)
            if tmp_max >= my_max :
                my_max = tmp_max 
                idx = min(idx,grid[i][j])
    print(f'#{t} {idx} {my_max}')