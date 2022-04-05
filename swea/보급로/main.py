import sys 
sys.stdin = open('input.txt','r')

import heapq
def djikstra() :

    while heap :
        #힙이 차있으면 
        #힙에서 가장 가까운 거리, r,c를 꺼내서 
        dist,r,c = heapq.heappop(heap)
        #네방향을 돈다. 
        for d in range(4) :
            nr = r + dr[d]
            nc = c + dc[d]
            #범위 안에 있으면서 
            if 0<=nr<N and 0<=nc<N :
                #최초 위치에서 nr,nc까지의 거리가 현재까지 온 거리에서 다음 거리보다 멀면  
                if distance[nr][nc] > dist +grid[nr][nc] :
                    #최초 위치에서 nr,nc까지의 거리 갱신 
                    distance[nr][nc] = dist + grid[nr][nc]
                    #힙에 넣어줌 
                    heapq.heappush(heap,(distance[nr][nc],nr,nc))
            if nr == N-1 and nc == N-1 :
                return 
INF = 1e9
dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())

for t in range(1,T+1) : 
    N =int(input())

    grid = [list(map(int,input())) for _ in range(N)]


    distance = [[INF]*N for _ in range(N)]
    heap = []
    distance[0][0] = 0
    #초기 출발 위치 힙에 넣기 
    heapq.heappush(heap,(0,0,0))
    djikstra()
    result = distance[N-1][N-1]
    print(f'#{t} {result}')


