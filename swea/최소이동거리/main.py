
# 방문하지 않는 노드 중에서, 가장 최단 거리의 노드 번호 반환 
def get_smallest_node() :
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1,N+1) :
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    #시작노드 초기화
    distance[start] = 0
    #방문처리 
    visited[start] = True

    #시작지점에서 갈 수 있는 경로들을 순회하면서 
    #j[0]로(b로) 갈 때 드는 코스트를 j[1]으로(c로) 입력 
    for j in graph[start] :
        distance[j[0]] = j[1]

    #시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(N-1) :
        #현재 최단거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = 1 
        #현재 노드와 연결된 다른 노드들 확인
        for j in graph[now] :
            cost = distance[now] + j[1]

            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost


T = int(input())

for t in range(1,2) : 
    INF = 10e9
    #마지막 지점 번호 N, 도로의 개수 
    N,E = map(int,input().split())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담을 리스트 만들기
    graph =[[] for _ in range(N+1)]

    #방문배열 만들기
    visited = [0]*(N+1)
    #최단거리 테이블을 무한으로 초기화
    distance = [INF]*(N+1)

    for _ in range(E) :
        #a에서 b까지 가는 비용이 c인 정보들을 받아와서 그래프에 넣기 
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
    dijkstra(0)
    print(f'#{t} {distance[N]}')




