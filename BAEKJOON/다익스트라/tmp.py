import heapq
import sys 

input = sys.stdin.readline
def solution(start) :

    #내 자신과의 거리는 0
    distance[start] = 0
    #힙 만들기 
    heap = []
    #내 자신과 비용은 0, 시작지점 넣기 
    heapq.heappush(heap,(0,start))

    for _ in graph :
        print(_)
    #힙이 차있을 때 
    while heap :
        #비용이 가장 적은 요소의 
        #비용과 현위치 빼기 
        print(heap)
        print(distance)
        cost,now = heapq.heappop(heap)
        print(now)
        print('-'*100)
        #현위치에서 갈 수 있는 정점과 비용을 확인 
        for next,weight in graph[now] :
            #다음 간선까지 비용은 출발점부터 현위치 + 다음 위치까지 비용
            cost2 = cost + weight 

            #현재 비용이 distance의 최소값보다 작으면 
            if cost2 < distance[next] :
                
                #next까지 갈 수 있는 비용 초기화 
                distance[next] = cost2
                #힙에 현재 비용과 다음 위치 넣기 
                heapq.heappush(heap,(cost2,next))





V,E = map(int,input().split())

K = int(input())

#인덱스 맞추기 위해 +1 부터 넣음
graph = [[]*V for _ in range(V+1)]

for _ in range(E) :
    #출발,도착,비용
    s,e,w = map(int,input().split())

    #도착지점과 비용 넣기 
    graph[s].append((e,w))

#시작지점에서 도착 위치는 모두 무한대로 초기화 
INF = int(1e9)
distance = [INF]*(V+1)

solution(K)

for ans in distance[1:] :
    if ans == INF :
        print('INF')
    else :
        print(ans)