import copy


R,C,T = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(R)]

dr = [0,-1,0,1]
dc = [1,0,-1,0]


dr2 = [0,1,0,-1]
dc2 = [1,0,-1,0]

time = 0 

stack = []
cleaner = []
for r in range(R) :
    for c in range(C) :
        if grid[r][c] > 0 :
            stack.append([r,c])
        elif grid[r][c] == -1  :
            cleaner.append([r,c])
downr,downc = cleaner.pop()
upr,upc = cleaner.pop()

while True :
    us = 0
    ds = 0
    if T == time :
        break

    new_grid = copy.deepcopy(grid)
  

    while stack :
        cr,cc=  stack.pop()
        cnt = 0
        plus = int(grid[cr][cc]/5)
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<=nr<R and 0<=nc<C and grid[nr][nc] >=0:
                new_grid[nr][nc] += plus
                cnt += 1
        else :
            new_grid[cr][cc] = new_grid[cr][cc]-(plus*cnt)

    upr2,upc2 = upr,upc
    next = 0
    before = 0
    while True : 
        nr = upr2+dr[us]
        nc = upc2+dc[us]
        if nr == upr and nc ==upc :
            break
        if nr<0 or nr>(R-1) or nc<0 or nc>(C-1) :
            nr -= (upr2+dr[us])
            nc -= (upc2+dc[us])
            us = (us+1)%4
            nr += upr2+dr[us]
            nc += upc2+dc[us]
        next = new_grid[nr][nc]
        new_grid[nr][nc] = before 
        before = next
        upr2,upc2=nr,nc

    downr2,downc2 = downr,downc
    next = 0
    before = 0
    while True : 
        nr = downr2+dr2[ds]
        nc = downc2+dc2[ds]
        if nr == downr and nc ==downc :
            break
        if nr<0 or nr>(R-1) or nc<0 or nc>(C-1) :
            nr -= (downr2+dr2[ds])
            nc -= (downc2+dc2[ds])
            ds = (ds+1)%4 
            nr += downr2+dr2[ds]
            nc += downc2+dc2[ds]
        #한칸 밀기 (현재값을 다음값으로 보내고 다음값을 저장)
        next = new_grid[nr][nc]
        new_grid[nr][nc] = before 
        before = next
        downr2,downc2 = nr,nc

    time += 1 
    grid = new_grid
    for r in range(R) :
        for c in range(C) :
            if grid[r][c] >0 :
                stack.append((r,c))

empty = 0

for r in range(R) :
    for c in range(C) :
        empty += grid[r][c]

print(empty+2)