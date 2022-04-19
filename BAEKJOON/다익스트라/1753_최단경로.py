import heapq
import sys 

input = sys.stdin.readline
#무한대 설정 
INF = 10e9

#정점 수, 간선수
V,E = map(int,input().split())

#그리드 만들기 
grid = [[]for _ in range(V+1)]
#시작점 받기 
start = int(input())

#간선을 돌면서 
for _ in range(E) :
    #출발 도착 비용 
    u,v,w = map(int,input().split())
    #추가하기 
    grid[u].append((v,w))

#거리 초기화 
distance = [INF]*(V+1)
#시작점은 0
distance[start] = 0
#힙 
heap = []

#힙에 출발점과 비용 넣기 
heapq.heappush(heap,(0,start))

#힙을 돌면서 
while heap :
    #비용과 현위치 
    cost,now = heapq.heappop(heap)
    #현위치에서 갈 수 있는 정점과 비용을 봐서 
    for next,weight in grid[now] :
        #다음 간선까지의 비용 계산 
        cost2 = cost + weight
        #원래 비용보다 적다면 
        if cost2 < distance[next] :
            #비용 갱신해주고 
            distance[next] = cost2
            #힙에 다시 추가  
            heapq.heappush(heap,(cost2,next))

#간선을 돌면서출력 
for i in range(1,V+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])