from collections import deque 
n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
dr = [0,-1,0,1]
dc = [1,0,-1,0]

rm = []
q = deque()
lst = []
remain = 0
visited =[]

# for i in grid :
#     print(i)
for r in range(n) :
    for c in range(m) :
        if r == 0 or c == 0 or r == n-1 or c == m-1 :
            grid[r][c] = -1 
            q.append([r,c])
            visited.append((r,c))
        elif grid[r][c] == 1 :
            remain += 1

cnt = 0
while True :
    cnt +=1 
    if rm :
        tmp_q = deque(rm[:])
    else :
        tmp_q = q
    rm = []
    tmp = 0
    while tmp_q :
        cr,cc = tmp_q.popleft()

        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d] 

            if 0<nr<n-1 and 0<nc<m-1 and not (nr,nc) in visited :
                if grid[nr][nc] == 1 :
                    rm.append([nr,nc])
                    grid[nr][nc] = 0
                    tmp +=1 
                elif grid[nr][nc] == 0 :
                    tmp_q.append([nr,nc])
                visited.append((nr,nc)) 
    remain = remain-tmp
 
    if remain == 0 :
        break

print(cnt)
print(tmp)