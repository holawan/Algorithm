N = int(input())
grid = [list(input()) for _ in range(N)]

disable = {'R' : 0, 'B' : 0}
able = {'R' : 0 , 'G' : 0, 'B' : 0}

dr = [0,1,0,-1]
dc = [1,0,-1,0]

cnt = 1 


visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]

for r in range(N) :
    for c in range(N) :
        if not visited[r][c] :
            stack = [(r,c)]
            color = grid[r][c]
            while stack  : 
                sr,sc = stack.pop()
                for d in range(4) :
                    nr = sr +dr[d]
                    nc = sc + dc[d]

                    if 0<=nr<N and 0<=nc<N and grid[nr][nc] == color and not visited[nr][nc]:
                        stack.append((nr,nc))
                        visited[nr][nc] = 1
                        if grid[r][c] == 'G' :
                            grid[r][c] = 'R'
        
            able[color] += 1
        if grid[r][c] == 'G' :
            grid[r][c] = 'R'

for r in range(N) :
    for c in range(N) :
        if not visited2[r][c] :
            stack = [(r,c)]
            color = grid[r][c]
            while stack  : 
                sr,sc = stack.pop()
                for d in range(4) :
                    nr = sr +dr[d]
                    nc = sc + dc[d]

                    if 0<=nr<N and 0<=nc<N and grid[nr][nc] == color and not visited2[nr][nc]:
                        stack.append((nr,nc))
                        visited2[nr][nc] = 1
        
            disable[color] += 1
                
print(sum(able.values()),sum(disable.values()))