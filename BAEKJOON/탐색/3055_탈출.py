# empty = . water = *, rock = 'X', biber = D go = 'S'

from collections import deque
#방향 설정 
dr = [0,1,0,-1]
dc = [1,0,-1,0]

n,m = map(int,input().split())

#물이 범람한 곳 
visit_water = []
#맵 받아오기 
grid = [list(input()) for _ in range(n)]
#방문배열 
visited = [[0]*m for _ in range(n)]
#그리드 돌면서 
wq = []
for r in range(n) :
    for c in range(m) :
        #도착지점 
        if grid[r][c] == 'D' :
            er,ec = r,c 
        #시작지점 
        elif grid[r][c] == 'S' :
            sr,sc = r,c 
            visited[r][c] = 1 
        #물이 있는 곳과 돌이 있는 곳 
        elif grid[r][c] == '*' :
            wq.append((r,c))
        elif grid[r][c] =='X' :
            visited[r][c] = 1
#시작지점에서 돌리는 큐 
qs = [(sr,sc)]+wq
q = deque(qs)
ans = 'KAKTUS'

#물큐와 고슴도치 큐를 돌면서 
while q :

    r, c = q.popleft()

    for d in range(4) :
        nr = r+dr[d]
        nc = c+dc[d]
        if 0<=nr<n and 0<=nc<m  :
            if grid[r][c] == 'S' and not visited[nr][nc] and (grid[nr][nc] == '.' or grid[nr][nc] == 'D') :
                visited[nr][nc] = visited[r][c] + 1 
                grid[nr][nc] = 'S'
                q.append((nr,nc))
                if nr==er and nc == ec :
                    ans = visited[r][c] 
            elif grid[r][c] == '*' and (grid[nr][nc] == 'S' or grid[nr][nc] == '.') :
                grid[nr][nc] = '*'
                q.append((nr,nc))

print(ans)
