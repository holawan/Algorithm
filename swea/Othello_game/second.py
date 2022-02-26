import sys 

sys.stdin = open('input.txt','r')

T = int(input())

#게임 조건 
#1. 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을때만 놓을 수 있다.
#그 때, 상대 돌은 자신의 돌이 된다. (사이란 가/세/대각)
#돌을 놓을수 없는 곳은 입력으로 주어지지 않는다. 

for t in range(1,T+1) :
    #게임판, 게임수 받아오기
    n,m = map(int,input().split())
    #게임판 만들기
    grid = [[0]*n for _ in range(n)] 
    #게임판 초기 세팅
    grid[n//2-1][n//2-1] = 'w'
    grid[n//2-1][n//2] = 'b'
    grid[n//2][n//2-1] = 'b'
    grid[n//2][n//2] = 'w'
    #돌을 놓았을 때, 범위를 벗어나지 않으면서 
    # [r-2][c] or [r][c-2] or [r+2][c] or [r][c+2] or [r-2][c-2]
    # [r+2][c+2] [r-2][c+2] or [r+2][c-2] 가 자신과 같으면 
    # -1한 값을 자신으로 변경 ??? 
    dr = [-1,0,1,0,-1,1,-1,1]
    dc = [0,-1,0,1,-1,1,1,-1]
    for game in range(m) :
            x,y,col = map(int,input().split())
            #돌을 grid[y-1][x-1]에 놓게된다!
            #좌표 내 방식으로 변경
            x,y = y-1,x-1 
            #흑돌일 때 
            if col == 1 :
                #흑돌을 놓는다. 
                if grid[x][y] :
                    continue
                else :
                    grid[x][y] = 'b'
                #흑돌의 주변 경우의 수를 모두 돌면서(+1된 경우 제외)  
                for k in range(n-1,1,-1) :
                    #상하좌우, 대각 4개를 탐색 
                    for i in range(8) :
                        #상하좌우로 x+k씩 탐색하며(k의 최소값은 2이므로 자신과 직접 닿아있는 부분 제외)
                        #new_k로 둔다. 
                        new_x = x+dr[i]*k ;new_y = y+dc[i]*k 
                        #범위 안에 있고, grid[new_x][new_y]가 같은 색이면 
                        if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y] == 'b':
                        #1부터 k-1만큼 해당 방향으로 순회하며
                            if grid[x+dr[i]*(k-1)][y+dc[i]*(k-1)] == 'w' :
                                    grid[x+dr[i]*(k-1)][y+dc[i]*(k-1)] = 'b' 

            elif col == 2 :
                if grid[x][y] :
                    continue
                else :
                    grid[x][y] = 'w'
                for k in range(n-1,1,-1) :
                    for i in range(8) :
                        new_x = x+dr[i]*k ;new_y = y+dc[i]*k 
                        if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y] == 'w'  :
                            if grid[x+dr[i]*(k-1)][y+dc[i]*(k-1)] == 'b' :
                                    grid[x+dr[i]*(k-1)][y+dc[i]*(k-1)] = 'w' 

    w_sum = 0
    b_sum = 0
    for r in range(n) :
        for c in range(n) :
            if grid[r][c] == 'w' :
                w_sum +=1 
            elif grid[r][c] == 'b' :
                b_sum +=1 
    print(f'#{t} {b_sum} {w_sum}')