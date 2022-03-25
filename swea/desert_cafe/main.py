import sys
sys.stdin = open('input.txt','r')


def dfs(i,j,visited,direction) :
    global ans,si,sj


    if direction > 3 :
        return
    if direction == 3 and i == si and j == sj and ans<len(visited) :
            ans = len(visited)
            return 
    ni = i + dr[direction]
    nj = j + dc[direction]
    if 0<=ni<n and 0<=nj<n and not grid[ni][nj] in visited :
        dfs(ni,nj,visited + [grid[ni][nj]],direction)

    if 0<=ni<n and 0<=nj<n and not grid[ni][nj]in visited :
        dfs(ni,nj,visited + [grid[ni][nj]],direction +1)

T = int(input())

#시계방향
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]

for t in range(1,T+1) :
    n = int(input())
    #그리드 만들기
    grid = [list(map(int,input().split())) for _ in range(n)] 
    
    #디저트종류 방문표시할 리스트
    #최초 정답은 먹을수 없는 경우
    ans = -1 

    #행열을 순회하며 
    for i in range(n) :
        for j in range(n) :
            #시작지점 입력 
            si,sj = i,j
            visited = []
            #디저트 종류에 방문표시 

            #현 시점에서 dfs로 탐색 
            dfs(si,sj,visited,0)


    print(f'#{t} {ans}')

