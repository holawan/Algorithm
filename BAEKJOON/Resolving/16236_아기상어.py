from collections import deque
N =int(input())

grid = [list(map(int,input().split())) for _ in range(N)]


dr = [-1,0,1,0]
dc = [0,-1,0,1]

for r in range(N):
    for c in range(N) :
        if grid[r][c] == 9 :
            sr,sc = r,c
            grid[r][c] = 2

visited = [[0]*N for _ in range(N)]

q = deque([(sr,sc,2)])

cnt = 0
visited[sr][sc] = 1
while q :
    r,c,size = q.popleft()
    for d in range(4) :
        nr = r+dr[d]
        nc = c+dc[d]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and grid[r][c] >= grid[nr][nc] :
            if grid[nr][nc] == grid[r][c] :
                q.append((nr,nc,size))
            elif grid[nr][nc] == 0 :
                visited[nr][nc] = visited[r][c] +1
                q.append((nr,nc,size))
                grid[nr][nc] = grid[r][c]
            elif grid[nr][nc] < grid[r][c] :
                visited[nr][nc] = visited[r][c] +1 
                q.append((nr,nc,size+1))
    else :
        grid[r][c] = 0

print(size)