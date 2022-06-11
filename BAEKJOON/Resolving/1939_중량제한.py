import heapq 

import sys 
input = sys.stdin.readline


INF = -1e9 
N,M = map(int,input().split())

grid = [[] for _ in range(N+1)]

visited = [-INF]*(N+1)

for _ in range(M) :
    a,b,c = map(int,input().split())
    #양방향이므로 둘다 추가 
    grid[a].append((b,-c))
    grid[b].append((a,-c))
#시작점 도착점 
f1,f2 = map(int,input().split())

heap = [(INF,f1)]

while heap :
    w,v = heapq.heappop(heap)
    if v == f2 :
        print(-w)
        break 
    for to,weight in grid[v] :
        if visited[to] <= weight :
            continue
        visited[to] = weight 
        heapq.heappush(heap,(max(w,weight),to))