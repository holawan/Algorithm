from collections import deque
import sys 

sys.stdin = open('input.txt','r')


def bfs() :
    #시계방향 설정 
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    #큐에 값이 있다면 
    while que :

        #현위치 r,c
        r,c = que.popleft()
        #시계방향을 탐색한다.  
        for i in range(4) :
            new_r = r + dr[i]
            new_c = c + dc[i]
            #만약 도착지라면 도착지 값이 3이기 때문에 2를 빼고 리턴한다. 
            if stop_x == new_r and stop_y == new_c :
                grid[new_r][new_c] = grid[r][c] -2 
                return grid[new_r][new_c]
                #범위에 있고 길이라면 
            if 0<=new_r<n and 0<=new_c<n and not(grid[new_r][new_c]) :
                #한걸음 더 간거기 때문에 현재 이동한 거리에 1을 추가한다. 
                grid[new_r][new_c] = grid[r][c] + 1 
                #현위치를 큐에 추가한다. 
                que.append([new_r,new_c])

T = int(input())

for t in range(1,T+1) :
    n = int(input())

    que = deque([])
    grid = [list(input()) for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            grid[i][j] = int(grid[i][j])
            #시작점을 큐에 넣는다. 
            if grid[i][j] == 2 :
                que.append([i,j])
            #도착지점을 입력해놓는다. 
            elif grid[i][j] == 3 :
                stop_x,stop_y = i,j
    result = bfs()

    if result == None :
        result = 0 
    print(f'#{t} {result}')
    

