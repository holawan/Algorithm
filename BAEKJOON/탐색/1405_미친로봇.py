def dfs(r, c, depth, p):
    global ans
    # print(p)
    #N번 겹치지 않고 도착했으면 단순한 것 
    #단순할 확률에 추가 
    if depth == N:
        ans += p
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        #방문했던 곳이면 진행x
        if grid[nr][nc]:
            continue
        #범위를 벗어나면 진행 x
        if not 0 <= nr < (2 * N) + 1 or not 0 <= nc < (2 * N) + 1:
            continue
        
        #방문처리 
        grid[nr][nc] = 1
        #새로운 곳이므로 
        #다음 위치로 가서 depth를 추가해주고, 해당 경로로 갈 확률 갱신해주기 
        dfs(nr, nc, depth + 1, p * direction[d] * 0.01)
        #방문취소 처리 
        grid[nr][nc] = 0


N, East,West,North,South = map(int,input().split())
direction = [East, West, North, South]
#동,서,남,북
dr = [0,0,1,-1]
dc = [1,-1,0,0]

grid = [[0]*(2*N+1) for _ in range(2*N+1)]

#로봇은 중앙에서 시작 
grid[N][N] = 1 

ans = 0

dfs(N, N, 0, 1)
print(ans)