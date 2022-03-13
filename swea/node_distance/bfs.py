from collections import deque
import sys 

sys.stdin = open('input_bfs.txt','r')


T = int(input())

for t in range(1,T+1) :

    node,route= map(int,input().split())
    grid = [[0]*(node+1) for _ in range(node+1)]
    for i in range(route) :
        a,b = map(int,input().split())
        grid[a][b] = 1
        grid[b][a] = 1 
    s,g = map(int,input().split())
    visited= [0]*(node+1)
    que = deque([s])
    visited[s] = 1 
    res = []
    while que :
        v = que.popleft()
        for i in range(1,node+1) :
            if grid[v][i] and not(visited[i]) :
                que.append(i)
                visited[i] += visited[v] + 1
            if visited[g] :
                res.append(visited[g])

    if res :
        ans = min(res)-1 
    else :
        ans = 0

    
    print(f'#{t} {ans}')
   
