import heapq
dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())
#초기 거리 
INF = 10e9
for t in range(1,T+1) : 
    n = int(input())

    #그래프 받아오기 
    grid = [list(map(int,input().split())) for _ in range(n)]
    #거리 무한대로 초기화 
    distance = [[INF]*n for _ in range(n)]
    #시작점은 0 
    distance[0][0] = 0

    #힙 만들기 
    heap = []
    #힙에 비용,시작점r,시작점c 입력해주기 
    heapq.heappush(heap,(0,0,0))

    #힙이 차있으면 
    while heap :
        #비용,행,열 꺼내서 
        cost,r,c = heapq.heappop(heap)
        #새로운 네방향 탐색 
        for d in range(4) :
            nr = r+dr[d]
            nc = c+dc[d]
            #범위 안에 있으면서 
            if 0<=nr<n and 0<=nc<n :
                #다음 위치가 나보다 높으면 그만큼 비용 +해주기 
                if grid[nr][nc] > grid[r][c] :
                    cost2 = cost + grid[nr][nc]-grid[r][c]
                #위치가 더 낮거나 같으면 그냥 비용 사용 
                else :
                    cost2 = cost
                #현재 nr까지 가는 비용이 현재 비용에서 +1 한 것보다 크면 
                if distance[nr][nc] > cost2 + 1 :
                    #비용갱신 
                    distance[nr][nc] = cost2 +1
                    #힙에 넣어주기 
                    heapq.heappush(heap,(distance[nr][nc],nr,nc))

    print(f'#{t} {distance[n-1][n-1]}')


