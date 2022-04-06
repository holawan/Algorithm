import heapq

INF = 10e9
T = int(input())
for t in range(1,T+1) : 
    #노드의 수, 간선의 수 
    n,e = map(int,input().split())

    #연결상태와 코스트를 나타낼 그래프 
    graph = [[] for _ in range(n+1)]

    for _ in range(e) :
        #a가 b까지 가는 비용 c 
        a,b,c = map(int,input().split())
        #그래프의 a칸에 b,c를 넣기 
        graph[a].append((b,c))

    #거리를 무한대로 초기화 
    distance = [INF]*(n+1)
    #출발지점은 비용 0 
    distance[0] = 0 

    #힙에 비용과 연결정보 넣기 
    heap = []
    heapq.heappush(heap,(0,0))

    while heap :
        #비용과 현위치 넣기 
        cost, now = heapq.heappop(heap)

        if distance[now] < cost :
            continue
        #현재 위치에서 갈 수 있는 곳을 돌면서 
        for i in graph[now] :
            #거쳐가는 비용은 현재까지 온 비용에서 다음 곳으로 가는 비용 
            cost2 = cost + i[1]
            #이 비용이 distance에 입력된 비용보다 적으면 
            if cost2 < distance[i[0]] :
                #이 거리가 더 짧은 것 
                distance[i[0]] = cost2
                #코스트랑 현재 위치 넣어주기  
                heapq.heappush(heap,(cost2,i[0]))
    
    result = distance[n]
    print(f'#{t} {result}')

