from collections import deque 


n, m = map(int,input().split())

jump = {}

for _ in range(n+m) :
    i,j = map(int,input().split())
    jump[i] = j 

grid = [0]*101 
visited= [0]*101 

q = deque([1])
visited[1] = 1 
while q :
    x = q.popleft()
    if x == 100 :
        break
    for i in range(1,7) :
        nx = x + i 
        #범위안에 있고 방문하지 않았으면 
        if 0<=nx<101 and not visited[nx] :
            #점프가능하면 점프 시킨다. 
            if nx in jump.keys() :
                nx = jump[nx]
            #점프 후에도 방문하지 않았다면 방문표시하고 큐에 추가하고 cnt += 1 
            if not visited[nx] :
                q.append(nx)
                visited[nx] = 1 
                grid[nx] = grid[x] + 1 
     
print(grid[100])
