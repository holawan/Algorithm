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
    grid[n//2-1][n//2-1] = 2
    grid[n//2-1][n//2] = 1
    grid[n//2][n//2-1] = 1
    grid[n//2][n//2] = 2

    
    #좌표 입력 
    dr = [-1,0,1,0,-1,1,-1,1]
    dc = [0,-1,0,1,-1,1,1,-1]
    for game in range(m) :
        x,y,col = map(int,input().split())
        #돌을 grid[y-1][x-1]에 놓게된다
        #좌표 내 방식으로 변경
        r,c = y-1,x-1 
        grid[r][c] =col
        
        #8방향을 돈다. 
        for k in range(8) :
            #탐색 
            nr = r + dr[k]
            nc = c + dc[k] 
            #바꿀 돌들을 담아줄 리스트
            lst = []

            #탐색한 위치에 돌이 없으면 아무것도 못함 
            if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0 :
                continue
            #탐색한 자리가 빈자리가 아니면서 내 색깔이 아닐 때 
            while 0<=nr<n and 0<=nc<n and grid[nr][nc]!=col and grid[nr][nc]!= 0 :
                #lst에 넣어주고 계속 바꿀 돌 탐색 
                lst.append([nr,nc])
                nr += dr[k]
                nc += dc[k]
            # 도착한 돌이 범위 내에 있으면서 나와 같은 색이면 
            if 0<=nr<n and 0<=nc<n and grid[nr][nc] == col:
                #사이에 있는 돌들의 색을 바꿔준다.
                for a,b in lst :
                    grid[a][b] =col

    #돌 숫자 세기 
    len_b = 0
    len_w = 0

    for r in range(n) :
        for c in range(n) :
            if grid[r][c] == 1 :
                len_b += 1 
            elif grid[r][c] == 2 :
                len_w += 1 
    print(f'#{t} {len_b} {len_w}')