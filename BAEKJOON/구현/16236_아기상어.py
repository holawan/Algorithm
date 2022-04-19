from collections import deque
N =int(input())

grid = [list(map(int,input().split())) for _ in range(N)]

#방향 
dr = [-1,0,1,0]
dc = [0,-1,0,1]

#물고기수 
fish = 0
#상어 최초 크기 
shark = 2

#먹은 물고기 수 
eat = 0

#아기상어 위치가 시작 위치
for r in range(N):
    for c in range(N) :
        #상어 위치 
        if grid[r][c] == 9 :
            sr,sc = r,c
            grid[r][c] = 0
        #물고기 수 
        elif 0<grid[r][c] <=6 :
            fish += 1 

#아기상어 시작 위치와 크기 배열에 넣기 

def bfs(sr,sc) :

    q = deque([(sr,sc,0)])

    #물고기까지 거리를 담을 리스트 
    dist_lst = [] 
    #방문배열 
    visited =[[0]*N for _ in range(N)]
    visited[sr][sc] = 1 

    min_dist = 1e9

    #큐가 빌때까지 
    while q :
        #꺼내고 
        r,c,dist = q.popleft()
        #4방향 탐색 
        for d in range(4) :
            nr = r + dr[d]
            nc = c + dc[d]
            #거리 안에 있으면서 방문하지 않았을 때 #나보다 작거나 같으면 방문한다. 
            if 0<=nr<N and 0<=nc <N and not visited[nr][nc] and grid[nr][nc] <= shark :
                visited[nr][nc] = 1 
                #상어보다 작으면 해당 상어까지 거리를 최소거리로 갱신하고 후보에 넣는다. 
                if 0< grid[nr][nc] < shark :
                    min_dist = dist 
                    dist_lst.append((nr,nc,dist+1))
                #한 칸 더 탐색할 곳이 최소거리보다 작다면 큐에 추가해서 탐색한다. 
                if dist + 1 <=min_dist :
                    q.append((nr,nc,dist+1 ))
        
    if dist_lst :
        dist_lst.sort(key=lambda x:(x[2],x[0],x[1]))
        return dist_lst[0]
        
#소요시간 
time = 0
#남은 물고기가 있을 때 
while fish :
    #현 위치에서 가장 가까우면서 먹을 수 있는 물고기를 찾는다. 
    result = bfs(sr,sc)

    #먹을 물고기가 없으면 멈춘다. 
    if not result :
        break 
    #물고기를 찾으면 그 위치가 내 자리 
    sr,sc = result[0],result[1]
    #걸린 시간에 물고기한테 가는데 걸린 거리를 더한다. 
    time += result[2]

    #먹은 물고기
    eat += 1 
    #남은 물고기 
    fish -=1 
    #상어 크기와 먹은 물고기가 같으면 
    if shark == eat :
        #상어 크기 더하고 
        shark += 1 
        #물고기 수 추가 
        eat = 0
    
    #물고기 먹었으니까 자리 없애기 
    grid[sr][sc] = 0
print(time)