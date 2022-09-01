import sys
input = sys.stdin.readline

n,m,rotation = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

for _ in range(rotation):
    #가장 바깥부터 돌리기 
    for i in range(min(n, m) // 2): 
        # print(i)
        r=i
        c =i
        temp = grid[r][c]
        
        #왼쪽으로 돌리기 
        for j in range(i + 1, n - i):  
            #가장 바
            r = j
            pre = grid[r][c]
            grid[r][c] = temp
            temp = pre

        for j in range(i + 1, m - i):  #아래 
            c = j
            pre = grid[r][c]
            grid[r][c] = temp
            temp = pre

        for j in range(i + 1, n - i):  #오른쪽 
            r = n - j - 1
            pre = grid[r][c]
            grid[r][c] = temp
            temp = pre

        for j in range(i + 1, m - i):  #위 
            c = m - j -1
            pre = grid[r][c]
            grid[r][c] = temp
            temp = pre

for r in range(n):
    for c in range(m):
        print(grid[r][c], end=' ')
    print()