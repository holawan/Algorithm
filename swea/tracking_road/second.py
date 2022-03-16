


T = int(input())
for t in range(1,T+1) : 
    n,k = map(int,input().split())

    grid = [list(map(int,input().split())) for _ in range(n)]

    ans = 0
    m = 0
    for i in range(n) :
        for j in range(n) :
            m = max(grid[i][j],m)
    
    for i in range(n) :
        for j in range(n) :
            if grid[i][j] == m :
                

