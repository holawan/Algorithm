import sys 

sys.stdin = open('input.txt','r')


dr = [0,-1,0,1]
dc = [1,0,-1,0]

def dfs(i,j) :
    global ans 

    for x in range(4) :
        new_i = i + dr[x]
        new_j = j + dc[x]
        if 0<=new_i<n and 0<=new_j<n  :
            if grid[new_i][new_j] == 3 :
                ans = 1 
                return  
            elif grid[new_i][new_j] == 0:
                grid[i][j] = -1 
                dfs(new_i,new_j)
                grid[i][j] = 0

T = int(input())

for t in range(1,T+1) :
    n = int(input())

    grid = [list(input()) for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            grid[i][j] = int(grid[i][j])
    for i in range(n) :
        for j in range(n) :
            if grid[i][j] == 2 :
                a,b = i,j 
                break
    ans = 0
    dfs(a,b)

    print(f'#{t} {ans}')


