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
wq = deque()
for r in range(n) :
    for c in range(m) :
        #도착지점 
        if grid[r][c] == 'D' :
            er,ec = r,c 
        #시작지점 
        elif grid[r][c] == 'S' :
            sr,sc = r,c 
        #물이 있는 곳과 돌이 있는 곳 
        elif grid[r][c] == '*' :
            wq.append((r,c))
            visit_water.append((r,c))
        elif grid[r][c] =='X' :
            visit_water.append((r,c))
#시작지점에서 돌리는 큐 
gq = deque([[sr,sc]])
#방문표시 
visited[sr][sc] = 1 
ans = 'KAKTUS'

#물큐와 고슴도치 큐를 돌면서 
while wq and gq :
    #고슴도치 큐 한사이클 돌리기 
    l2 = len(gq) 
    for _ in range(l2) :
        cr2,cc2 = gq.popleft()
        #현위치가 물이나 돌이 아니면 
        if not (cr2,cc2) in visit_water :
            #네방향 탐색 
            for d in range(4) :
                nr2 = cr2+dr[d]
                nc2 = cc2+dc[d]
                #현위치를 .으로 바꿔줌 
                grid[cr2][cc2] = '.'
                #범위 안에 있으면서 범람하지 않았으면 
                if 0<=nr2<n and 0<=nc2<m  and not (nr2,nc2) in visit_water  :
                    #빈곳일때 
                    if grid[nr2][nc2] == '.'  :
                        #방문 1 추가 
                        visited[nr2][nc2] = visited[cr2][cc2] + 1 
                        #S로 변경 
                        grid[nr2][nc2] = 'S'
                        #큐에 추가 
                        gq.append((nr2,nc2))
                    #도착지면 끝내기 
                    elif grid[nr2][nc2] == 'D' :
                        ans = visited[cr2][cc2] + 1
                        gq.clear()
                        print(ans-1)
                        exit() 
    #물큐 돌리기 
    l = len(wq) 
    #물큐 한사이클 
    for _ in range(l):
        cr1,cc1 = wq.popleft()
        #네방향 탐색 
        for d in range(4) :
            nr1 = cr1+dr[d]
            nc1 = cc1+dc[d]
            #범위 안에 있으면서 고슴도치나 빈곳이고 방문하지 않았으면 
            if 0<=nr1<n and 0<=nc1<m and (grid[nr1][nc1] == '.' or grid[nr1][nc1] == 'S') and not (nr1,nc1) in visit_water :
                #물채우기
                grid[nr1][nc1] = '*'
                visit_water.append((nr1,nc1))
                wq.append((nr1,nc1))


print(ans)
