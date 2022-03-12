import sys
sys.stdin = open('input.txt','r')


def dfs(i,j,direction,cnt) :
    global ans 

    #직진하거나 방향 전환을 위한 tmp 
    tmp = direction + 2 
    if tmp == 5 :
        tmp = 4
    
    #방향전환을 위한 for문 
    for k in range(direction,tmp) :
        new_i = i + dr[k]
        new_j = j + dc[k]

        #시작점으로 돌아오면 answer과 cnt를 비교해서 더 높은값을 ans로 
        if start[0] == new_i and start[1] == new_j :
            ans = max(ans,cnt)
            return

        #범위안에 있으면서
        if 0<=new_i<n and 0<=new_j<n :
            #방문하지 않았다면
            if not(visited[grid[new_i][new_j]]) :
                #방문표시 
                visited[grid[new_i][new_j]] = 1 

                dfs(new_i,new_j,k,cnt + 1)
                #방문표시 취소 
                visited[grid[new_i][new_j]] = 0
        #범위를 벗어나면 방향전환 
T = int(input())

#시계방향
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]

for t in range(1,T+1) :
    n = int(input())
    #그리드 만들기
    grid = [list(map(int,input().split())) for _ in range(n)] 
    
    #디저트종류 방문표시할 리스트
    visited = [0]*101 
    #최초 정답은 먹을수 없는 경우
    ans = -1 

    #행열을 순회하며 
    for i in range(n) :
        for j in range(n) :
            #시작지점 입력 
            start = [i,j] 
            #디저트 종류에 방문표시 
            visited[grid[i][j]] = 1 

            #현 시점에서 dfs로 탐색 
            dfs(i,j,0,1)

            visited[grid[i][j]] = 0

    print(f'#{t} {ans}')

