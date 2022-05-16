R,C,T = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(R)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]
dr2 = [0,-1,0,1]
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
up = [cleaner[0]]
down = [cleaner[1]] 
us = 0
ds = 0

while True :
    if T == time :
        break 
    new_stack = []
    

    while stack :
        cr,cc=  stack.pop()
        cnt = 0
        plus = int(grid[cr][cc]/5)
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<=nr<R and 0<=nc<C and grid[nr][nc] >=0:
                grid[nr][nc] += plus
                new_stack.append((nr,nc))
                cnt += 1
        else :
            grid[cr][cc] = grid[cr][cc]-(plus*cnt)
    stack = new_stack 

    upr,upc = up.pop()

    nr = upr+dr[us]
    nc = upc+dc[us]
    if nr<0 or nr>(R-1) or nc<0 or nc>(R-1) :
        nr -= (upr+dr[us])
        nc -= (upc+dc[us])
        us = (us+1)%4 
        nr += upr[0]+dr[us]
        nc += upc[1]+dc[us]
    up.append((nr,nc))

    downr,downc = down.pop()

    nr = downr+dr[ds]
    nc = downc+dc[ds]
    if nr<0 or nr>(R-1) or nc<0 or nc>(R-1) :
        nr -= (downr+dr[ds])
        nc -= (downc+dc[ds])
        ds = (ds+1)%4 
        nr += downr+dr[ds]
        nc += downc+dc[ds]
    down.append((nr,nc))
    
    time += 1 

empty = 0

for r in range(R) :
    for c in range(C) :
        empty += grid[r][c]

empty +=2 
print(empty)

for r in grid :
    print(r)

