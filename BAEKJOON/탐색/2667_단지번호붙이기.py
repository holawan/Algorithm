from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

n = int(input())
def bfs(i,j) :
    cnt = 0
    que = deque()
    que.append([i,j])
    visited[i][j] = 1
    cnt += 1 
    while que :
        s_i,s_j = que.popleft()
        for k in range(4) :
            n_i = s_i +dr[k]
            n_j = s_j +dc[k]
            if 0<= n_i<n and 0<=n_j<n and not visited[n_i][n_j] and grid[n_i][n_j]:
                que.append([n_i,n_j])
                visited[n_i][n_j] = 1 
                cnt += 1
    return cnt 

#그리드
grid= [list(map(int,input())) for _ in range(n)]
#방문배열 
visited = [[0]*n for _ in range(n)]
#정답을 넣을 배열 
ans = [] 
#아파트면서 방문하지 않았으면 
#bfs돌리기 
for i in range(n) :
    for j in range(n) :
        if grid[i][j]== 1 and not visited[i][j] : 
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
for i in ans :
    print(i)