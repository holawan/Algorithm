from collections import deque


N =int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]
visited = [[0]*N for _ in range(N)]
tmp = 1
#섬별로 번호 부여하기 

for r in range(N) :
    for c in range(N) :
        #방문하지 않은 섬이면 
        if grid[r][c] and not visited[r][c] : 
            #번호 올리고, 
            tmp += 1 
            #번호 부여 
            grid[r][c] = tmp
            #방문처리 
            visited[r][c] = 1
            q = deque([(r,c)])
            #속한 섬들 모두 번호 부여 
            while q :
                cr,cc = q.popleft()
                # print(cr,cc)
                for d in range(4) :
                    nr = cr + dr[d] 
                    nc = cc + dc[d] 
                    #범위 안에 있으면서 섬이면, 
                    if 0<=nr<N and 0<=nc<N and grid[nr][nc] and not visited[nr][nc] : 
                        grid[nr][nc] = tmp 
                        visited[nr][nc] = 1 
                        q.append((nr,nc))


bridge = 1e9 
#모든 행렬을 순회하며 
for r in range(N) :
    for c in range(N) :
        #네방향을 돌면서 
        if grid[r][c] > 0:
            for d in range(4) :
                nr = r + dr[d]
                nc = c + dc[d]
                #섬이 아니고 방문하지 않았으면 해당 바다(?)에서 출발한다. 
                if 0<=nr<N and 0<=nc<N and grid[nr][nc] ==0 :
                    #방문배열에 넣고 
                    visited  = [[0]*N for _ in range(N)]
                    #큐에 넣는다. 
                    q = deque([(nr,nc)])
                    visited[nr][nc] = 1 
                    #큐가 빌때까지 
                    x = 0
                    while q :
                        if x :
                            break
                        # print(q)
                        #꺼내고 
                        
                        cr,cc = q.popleft()
            
                        if visited[cr][cc] > bridge :
                            break
                        #아직 바다이면 4방향 돌면서 
                        for d in range(4) :
                            nr2 = cr + dr[d]
                            nc2 = cc + dc[d]
                            #범위안에 있으면서 방문하지 않았고, 내가 출발한 섬이 아니면 
                            if 0<=nr2<N and 0<=nc2<N and not visited[nr2][nc2] and grid[nr2][nc2] != grid[r][c] :
                                #바다일떄 
                                if grid[nr2][nc2] == 0 : 
                                    #큐에넣고 
                                    q.append((nr2,nc2))
                                    #방문배열에도 넣는다 .
                                    visited[nr2][nc2] = visited[cr][cc] + 1 
                                #섬일떄 
                                elif grid[nr2][nc2] != grid[r][c] : 
                                    # print(nr2,nc2,r,c,visited[cr][cc])
                                    if visited[cr][cc] < bridge :
                                        bridge = visited[cr][cc]
                                        # print(bridge)
                                        # print(cr,cc)
                                        x = 1 
print(bridge)
