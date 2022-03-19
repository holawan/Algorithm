T = int(input())

for t in range(1,T+1) : 
    n = int(input())
    grid = [list(map(int,input().split())) for _ in range(n)]

    dr = [0,-1,0,1]
    dc = [1,0,-1,0]

    visited = [[0]*n for _ in range(n)]
    def func(i,j) :
        global my_max 
        visited[i][j] = 1
        my_max +=1  
        for k in range(4) :
            ni = i+dr[k]
            nj = j+dc[k]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and grid[i][j]+1 == grid[ni][nj] :
                func(ni,nj)


    ans = []
    for i in range(n) :
        for j in range(n) :
            my_max = 0

            func(i,j)
            ans.append([grid[i][j],my_max])

    ans.sort(key= lambda x: (-x[1],x[0]))
    print(f'#{t} {ans[0][0]} {ans[0][1]}')