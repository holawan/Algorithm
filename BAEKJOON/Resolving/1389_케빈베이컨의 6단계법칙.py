from collections import deque


def bfs(graph,start) :

    num = [0]*(N+1)
    
    visited = [0]*(N+1) 
    visited[start] = 1 

    q = deque()
    q.append(start) 

    while q :
        x = q.popleft() 
        for i in grid[x] :
            if not visited[i] :
                num[i] = num[x] + 1
                visited[i] = 1 
                q.append(i)

    return sum(num)

N,M = map(int,input().split())

grid = [[]*(N) for _ in range(N+1)]


for i in range(M) :

    a,b = map(int,input().split())

    grid[a].append(b)
    grid[b].append(a) 


res = []

for i in range(1,N+1) :
    res.append(bfs(grid,i))

print(res.index(min(res))+1)
