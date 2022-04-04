# empty = . water = *, rock = 'X', biber = D go = 'S'

from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

n,m = map(int,input().split())

grid = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for r in range(n) :
    for c in range(m) :
        if grid[r][c] == 'D' :
            er,ec = r,c 
        elif grid[r][c] == 'S' :
            sr,sc = r,c 
        elif grid[r][c] == '*' :
            wr,wc = r,c
gq = deque([[sr,sc]])
wq = deque([[wr,wc]])
visited[sr][sc] = 1 
visit_water = [(wr,wc)]
ans = 'KAKTUS'
while wq and gq :

    l2 = len(gq) 
    for _ in range(l2) :
        cr2,cc2 = gq.popleft()
        if not (cr2,cc2) in visit_water :
            for d in range(4) :
                nr2 = cr2+dr[d]
                nc2 = cc2+dc[d]
                grid[cr2][cc2] = '.'
                if 0<=nr2<n and 0<=nc2<m  and not (nr2,nc2) in visit_water  :
                    if grid[nr2][nc2] == '.'  :
                        visited[nr2][nc2] = visited[cr2][cc2] + 1 
                        grid[nr2][nc2] = 'S'
                        gq.append((nr2,nc2))
                    elif grid[nr2][nc2] == 'D' :
                        ans = visited[cr2][cc2] + 1
                        gq.clear()
                        print(ans-1)
                        exit() 
    l = len(wq) 
    for _ in range(l):
        cr1,cc1 = wq.popleft()

        for d in range(4) :
            nr1 = cr1+dr[d]
            nc1 = cc1+dc[d]

            if 0<=nr1<n and 0<=nc1<m and (grid[nr1][nc1] == '.' or grid[nr1][nc1] == 'S') and not grid[nr1][nc1] == 'X' and not (nr1,nc1) in visit_water :
                grid[nr1][nc1] = '*'
                visit_water.append((nr1,nc1))
                wq.append((nr1,nc1))

print(ans)



        

