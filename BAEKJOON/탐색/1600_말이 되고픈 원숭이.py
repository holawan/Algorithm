#원숭이의 움직임 
from collections import deque


dr = [-1,0,1,0]
dc = [0,1,0,-1]
#말의 움직임 
dr2 = [-2,-2,-1,-1,1,1,2,2]
dc2 = [-1,1,-2,2,-2,2,-1,1]



K = int(input())
M,N = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

sr,sc = 0,0
er,ec = N-1,M-1

def bfs() : 
    q = deque([(sr,sc,K)])
    visited = [[[0 for _ in range(31)] for _ in range(M)] for _ in range(N)]
    while q :
        cr,cc,k = q.popleft()
        if cr==er and cc == ec :
            return visited[cr][cc][k]
        if k >0 :
            for d2 in range(8) :
                nr = cr + dr2[d2]
                nc = cc + dc2[d2]

                if 0<=nr<N and 0<=nc<M and visited[nr][nc][k-1]==0 and grid[nr][nc] == 0:
                    visited[nr][nc][k-1] = visited[cr][cc][k] + 1 
                    q.append((nr,nc,k-1))

        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d] 

            if 0<=nr<N and 0<=nc<M and  visited[nr][nc][k]==0 and grid[nr][nc] == 0:
                visited[nr][nc][k] = visited[cr][cc][k] + 1 
                q.append((nr,nc,k))
    return -1 
print(bfs())