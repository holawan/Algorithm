import sys


sys.stdin = open('input.txt','r')

def dfs(x,y) :
    global cnt
    cnt += 1
    if cnt == 3 :
        return

    info = R*x + y
    visited[info] = 1
    for i in range(0, len(visited), C):
        print(visited[i:R + i + 1])
    print('-----------------')
    for i in range(R) :
        for j in range(C) :
            if grid_2[i][j] == 1 and not(visited[R*i+j]) :
                dfs(i,j)


T = int(input())
R,C,r,c,L = map(int,input().split())
#N = 세로,M은 가로 맨홀위치 세로 R 가로 C 시간 L

grid = [list(map(int,input().split())) for _ in range(R)]

grid_2 = [[0]*C for _ in range(R)]

dr = [0,-1,0,1]
dc = [1,0,-1,0]

#그리드를 돌며
for i in range(R):
    for j in range(C) :
        if grid[i][j] == 1 :
            grid_2[i][j] = 1
            for x in range(4) :
                new_i = i + dr[x]
                new_j = j + dc[x]
                if 0<=new_i<R and 0<=new_j<C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] =1

        elif grid[i][j] == 2 :
            grid_2[i][j] = 1
            for x in range(1,5,2):
                new_i = i + dr[x]
                new_j = j + dc[x]
                if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] = 1
        elif grid[i][j] == 3 :
            grid_2[i][j] = 1
            for x in range(0, 4, 2):
                new_i = i + dr[x]
                new_j = j + dc[x]
                if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] = 1
        elif grid[i][j] == 4 :
            grid_2[i][j] = 1
            for x in [[1,0],[0,1]]:
                new_i = i + dr[x][0]
                new_j = j + dc[x][1]
                if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] = 1
        elif grid[i][j] == 5 :
            grid_2[i][j] = 1
            for x in [[-1, 0], [0, 1]]:
                new_i = i + dr[x[0]]
                new_j = j + dc[x[1]]
                if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] = 1
        elif grid[i][j] == 6 :
            grid_2[i][j] = 1
            for x in [[-1, 0], [0, -1]]:
                new_i = i + dr[x[0]]
                new_j = j + dc[x[1]]
                if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] = 1
        elif grid[i][j] == 7 :
            grid_2[i][j] = 1
            for x in [[1, 0], [0, -1]]:
                new_i = i + dr[x[0]]
                new_j = j + dc[x[1]]
                if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j]:
                    grid_2[new_i][new_j] = 1
cnt = 1
visited = [0]*(R*C)

dfs(r-1,c-1)

