from collections import deque 
N = int(input())
sr,sc,er,ec = map(int,input().split())

#체스판과 방문표시 만들기 
grid = [[0]*N for _ in range(N)]
visited= [[0]*N for _ in range(N)]

#큐에 시작점 넣기 
q = deque([[sr,sc]])
visited[sr][sc] = 1 

#이동 반경 
dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]

#bfs 돌리기 
while q :
    r,c = q.popleft()
    if r == er and c == ec :
        break 
    for d in range(6) :
        nr = r+ dr[d]
        nc = c + dc[d]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] :
            q.append([nr,nc])
            grid[nr][nc] = grid[r][c]+1 
            visited[nr][nc] = 1 

if grid[er][ec] :
    ans = grid[er][ec]
else :
    ans = -1 
print(ans)