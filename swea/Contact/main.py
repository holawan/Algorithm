import sys 

sys.stdin = open('input.txt','r')
from collections import deque

for t in range(1,11) : 
    n,start = map(int,input().split())

    grid = [[0]*101 for _ in range(101)]

    lst = list(map(int,input().split()))

    for i in range(0,n,2) :
        grid[lst[i]][lst[i+1]] = 1
    que = deque([start])
    visited = [0]*101 
    visited[start] = 0
    my_max = 0
    my_idx = 0
    while que :
        x = que.popleft()
        
        for i in range(101) :
            if grid[x][i] == 1 and not visited[i] :
                que.append(i)
                visited[i] = visited[x] + 1 
    my_max = max(visited)
    for i in range(100,-1,-1) :
        if visited[i] == my_max :
            my_idx = i 
            break 
    print(f'#{t} {my_idx}')
