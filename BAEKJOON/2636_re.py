from collections import deque 
n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
dr = [0,-1,0,1]
dc = [1,0,-1,0]

rm = []
q = deque()
lst = []
remain = 0

for i in range(n) :
    remain += sum(grid[i])
    grid[i][0],grid[i][m-1] = -1,-1 

grid[0] = [[-1]*m][:]
grid[n-1] = [[-1]*m][:]

for i in grid :
    print(i)
cnt = 0

visited =[]
while True :
    cnt +=1 
    if rm :
        tmp_q = deque(rm[:])
    else :
        tmp_q = q
    rm = []
    while tmp_q :
        cr,cc = tmp_q.popleft()
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d] 

            if 0<nr<n-1 and 0<nc<n-1 and not (nr,nc) in visited :
                if grid[nr][nc] == 1 :
                    rm.append([nr,nc])
                else :
                    tmp_q.append([nr,nc])
                visited.append((nr,nc)) 
    for rr,rc in rm :
        grid[rr][rc] = 0

    remain -= len(rm)

    if remain == 0 :
        break

print(cnt)
print(len(rm))