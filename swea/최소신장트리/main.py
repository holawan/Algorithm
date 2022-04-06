import heapq

T = int(input())
INF = 10e9

for t in range(1,T+1) : 
    v,e = map(int,input().split())

    graph = [[] for _ in range(v+1)]

    for _ in range(e) :
        a,b,c = map(int,input().split())

        graph[a].append((c,a,b))
        graph[b].append((c,b,a))

    heap = graph[0]
    visited = {0}
    mst = []
    heapq.heapify(heap)

    while len(visited) <= v and heap :
        cost,s,e = heapq.heappop(heap) 

        if e not in visited :
            visited.add(e)
            mst.append((cost,s,e))

            for route in graph[e] :
                if route[2] not in visited :
                    heapq.heappush(heap,route)
    print(mst)
    print(f'#{t} {sum(map(lambda x:x[0],mst))}')

#

