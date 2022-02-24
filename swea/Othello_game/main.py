import sys

sys.stdin = open('input.txt','r')
T = int(input())
n,m = map(int,input().split())
grid = [[0]*(n) for _ in range(n)]



#-1은 흑돌 1은 백돌
grid[n//2-1][n//2-1] = 'w'
grid[n//2][n//2-1] = 'b'
grid[n//2-1][n//2] = 'b'
grid[n//2][n//2] ='w'
# for i in grid :
#     print(i)
# print('--------------------')

#y = 열 x=행
for _ in range(10) :
    for i in grid:
        print(i)
    print('---------------')
    y, x, col = map(int,input().split())
    y = y-1 ; x = x-1
    if col == 1 :
        if (x+2<n and grid[x+2][y] == 'b') or (y+2<n and grid[x][y+2] == 'b') or (x-2>=0 and grid[x-2][y] == 'b') or (y-2>=0 and grid[x][y-2] == 'b') :
            grid[x][y] = 'b'
            if x+1<n and grid[x+1][y] =='w' :
                grid[x+1][y] = 'b'
            if y+1<n and grid[x][y+1] == 'w':
                grid[x][y+1] = 'b'
            if x-1>=0 and grid[x-1][y] == 'w' :
                grid[x-1][y] = 'b'
            if y-1>=0 and grid[x][y-1] == 'w' :
                grid[x][y-1] = 'b'
            if y-1>=0 and x-1>=0 and grid[x-1][y-1] == 'w' :
                grid[x-1][y-1] = 'b'
            if y+1<n and x+1<n and grid[x+1][y+1] == 'w' :
                grid[x+1][y+1] = 'b'
            if y+1<n and x-1>=0 and grid[x-1][y+1] == 'w' :
                grid[x-1][y+1] = 'b'
            if y-1>=0 and x+1<n and grid[x+1][y-1] == 'w' :
                grid[x+1][y-1] = 'b'
        else :
            continue

    elif col==2 :
        if (x+2<n and grid[x+2][y] == 'w') or (y+2<n and grid[x][y+2] == 'w') or (x-2>=0 and grid[x-2][y] == 'w') or (y-2>=0 and grid[x][y-2] == 'w') :
            grid[x][y] = 'w'
            if x+1<n and grid[x + 1][y] == 'b':
                grid[x + 1][y] = 'w'
            if y+1<n and grid[x][y + 1] == 'b':
                grid[x][y + 1] = 'w'
            if x-1>=0 and grid[x - 1][y] == 'b':
                grid[x - 1][y] = 'w'
            if y-1>=0 and grid[x][y - 1] == 'b':
                grid[x][y - 1] = 'w'
            if y-1>=0 and x-1>=0 and grid[x-1][y-1] == 'b' :
                grid[x-1][y-1] = 'w'
            if y+1<n and x+1<n and grid[x+1][y+1] == 'b' :
                grid[x+1][y+1] = 'w'
            if y+1<n and x-1>=0 and grid[x-1][y+1] == 'b' :
                grid[x-1][y+1] = 'w'
            if y-1>=0 and x+1<n and grid[x+1][y-1] == 'b' :
                grid[x+1][y-1] = 'w'
        else :
            continue
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid)) :
            if not(grid[i][j]) :
                cnt += 1
    if cnt == n**2 :
        break

