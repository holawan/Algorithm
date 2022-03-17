import sys 
from collections import deque
sys.stdin = open('maze1.txt','r')


dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = 10 
for _ in range(T) :
    t = int(input())
    #미로의 크기 
    n = 16

    #미로 리스트로 받아오기
    grid = [list(input()) for _ in range(n)]

    #큐 만들기
    que = deque()
    
    #행렬 돌면서 숫자로 변환하고 시작점 확인하기 
    for i in range(n) :
        for j in range(n)  :
            grid[i][j] = int(grid[i][j])
            if grid[i][j] == 2 :
                que.append((i,j))

    #최초 정답은 0 
    ans = 0
    #큐가 빌때까지
    while que :
        #출발점 꺼내서 
        r,c = que.popleft()
        #벽으로 만들고
        grid[r][c] = 1 

        #델타탐색 진행
        for k in range(4) :
            new_r = r + dr[k]
            new_c = c + dc[k]
            #갈 수 있을 때  
            if 0<=new_r<n and 0<=new_c<n  :
                #길이면 가고 
                if grid[new_r][new_c] == 0 :
                    que.append((new_r,new_c))
                #도착점이면 끝내기 
                elif grid[new_r][new_c] == 3 :
                    que = []
                    ans = 1 
                    break
    print(f'#{t} {ans}')