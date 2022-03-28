import sys 
sys.stdin = open('input.txt','r')

from collections import deque 

dr = [0,1,0,-1]
dc = [1,0,-1,0]


def bfs(sr,sc) :
    global ans 
    #방문표시
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1 

    que = deque()
    #현위치부터 시작 
    que.append([sr,sc])

    #집이 있으면 집 개수에 표시 
    home = grid[sr][sc]
    
    dis = 1 

    if home * M - klst[dis]>=0 :
        ans = max(home,ans)
    
    while dis<N+2 :
        for _ in range(len(que)) :
            r,c = que.popleft()
            for d in range(4) :
                nr = r + dr[d]
                nc = c + dc[d]

                if 0<=nr<N and 0<=nc <N and not visited[nr][nc] :
                    visited[nr][nc] = 1 
                    que.append([nr,nc])
                    if grid[nr][nc] :
                        home += 1 
        if home*M - klst[dis+1] >= 0 :
            ans = max(home,ans)
        dis += 1 

T = int(input())

for t in range(1,T+1) :
    N,M = map(int,input().split())
    grid=  [list(map(int,input().split())) for _ in range(N)]
    klst = [k**2+(k-1)**2 for k in range(N+3)]
    print(klst)
    ans = 0
    for i in range(N) :
        for j in range(N) :
            bfs(i,j)
    print(f'#{t} {ans}')