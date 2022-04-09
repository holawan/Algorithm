import heapq

INF = 10e9

V,E = map(int,input().split())

grid = [[]*(V+1)for _ in range(V+1)]
start = int(input())
for _ in range(E) :
    u,v,w = map(int,input().split())
    grid[u].append((v,w))

distance = [INF]*(V+1)
distance[start] = 0

heap = []

heapq.heappush(heap,(0,start))


while heap :
    cost,now = heapq.heappop(heap)
    
    if distance[now] < cost :
        continue
    for next in grid[now] :
        cost2 = cost + next[1] 

        if cost2 < distance[next[0]] :
            distance[next[0]] = cost2 
        heapq.heappush(heap,(cost2,next[0]))
for i in range(1,V+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])