dr = [1,0,-1,0,-1,-1,1,1]
dc = [0,1,0,-1,-1,1,1,-1]

while True :
    m,n = map(int,input().split())
    if n== 0 and m  == 0 :
        break 
    grid = [list(map(int,input().split())) for _ in range(n)]

    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for r in range(n) :
        for c in range(m) :

            if not visited[r][c] and grid[r][c] :
                lst = [(r,c)]
                while lst :
                    cr,cc = lst.pop()

                    for d in range(8) :
                        nr = cr + dr[d]
                        nc = cc + dc[d]

                        if 0<=nr<n and 0<=nc<m and grid[nr][nc] and not visited[nr][nc] :
                            lst.append((nr,nc))
                            visited[nr][nc] = 1 

                cnt += 1 
    print(cnt)

