from collections import deque
N =int(input())

grid = [list(map(int,input().split())) for _ in range(N)]

#방향 
dr = [-1,0,1,0]
dc = [0,-1,0,1]

#아기상어 위치가 시작 위치, 아기상어의 크기를 2로 변경 
for r in range(N):
    for c in range(N) :
        if grid[r][c] == 9 :
            sr,sc = r,c
            grid[r][c] = 0

#방문배열 
visited = [[0]*N for _ in range(N)]

#아기상어 시작 위치와 크기 배열에 넣기 
q = deque([(sr,sc)])

#시간 
cnt = 0
#아기상어 위치 방문표시 
visited[sr][sc] = 1
size = 2
while q :
    r,c = q.popleft()
    tmp_sum = 0
    for xr in range(N) :
        for xc in range(N) :
            tmp_sum += grid[xr][xc]
    if tmp_sum == 0 :
        break 
    #네방향 돌면서 
    for d in range(4) :
        nr = r+dr[d]
        nc = c+dc[d]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and size >= grid[nr][nc] :
            #크기가 같으면 넣기만하고 움직임 
            if grid[nr][nc] == size :
                q.append((nr,nc))
            #0이면 방문표시하고 지나감 
            elif grid[nr][nc] == 0 :
                q.append((nr,nc))
            #더 작으면 방문표시하고 size를 늘린다.
            elif grid[nr][nc] < size :
                visited[nr][nc] =  visited[r][c] +1
                q.append((nr,nc))
                grid[nr][nc] = 0
                cnt += 1 
    if cnt== size :
        size += 1 
        cnt = 0
                

for r in visited:
    print(r)
    cnt = max(max(r),cnt)
print(cnt-1) 
print('-------------')
for r in grid :
    print(r)
