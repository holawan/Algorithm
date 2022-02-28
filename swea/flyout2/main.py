import sys
sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1) :
    n,m = map(int,input().split())

    grid = [list(map(int,input().split())) for _ in range(n)]

    res = []
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    drr = [-1,1,1,-1]
    dcc = [1,1,-1,-1]
    for r in range(n):
        for c in range(n) :
            tmp = grid[r][c]
            for k in range(1,m) :
                for j in range(4):
                    nr,nc = r+dr[j]*k ,c+dc[j]*k 
                    if 0<=nr<n and 0<=nc<n :
                        tmp += grid[nr][nc]
            res.append(tmp)

            tmp_cross = grid[r][c]

            for k in range(1,m) :
                for j in range(4) :
                    nr,nc = r+drr[j]*k,c+dcc[j]*k 
                    if 0<=nr <n and 0<=nc<n :
                        tmp_cross += grid[nr][nc]
            res.append(tmp_cross)
    print(f'#{t} {max(res)}')