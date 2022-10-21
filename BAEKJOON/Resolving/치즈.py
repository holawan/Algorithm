import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]


def bfs():
    q = deque([(0,0)])
    visited[0][0] = 1
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<n and 0<=nc<m and visited[nr][nc] == 0:
                if grid[nr][nc] >= 1:
                    grid[nr][nc] += 1
                else:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
time = 0
while True:
    visited = [[0]*m for _ in range(n)]
    bfs()
    is_cheeze = False 
    for r in range(n):
        for c in range(m):
            if grid[r][c] >= 3:
                grid[r][c] = 0
                is_cheeze = True
            elif grid[r][c] == 2:
                grid[r][c] = 1
    if is_cheeze :
        time += 1
    else:
        break

print(time)