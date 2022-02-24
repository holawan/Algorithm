T = int(input())
for t in range(1,T+1) :
    n = int(input())

    grid = [[0]*n for _ in range(n)]

    num = 1

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    x = 0
    y = 0
    direction = 0
    while num <= n**2 :
        grid[x][y] = num 
        x += dx[direction]
        y += dy[direction]

        if y<0 or x<0 or y>= n or x>=n or grid[x][y] :
            x -= dx[direction]
            y -= dy[direction]
            
            direction = (direction+1)%4

            x += dx[direction]
            y += dy[direction]
        num += 1 

    print(f'#{t}')
    for i in grid:
        print(*i)