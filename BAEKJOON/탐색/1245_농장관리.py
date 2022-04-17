
# dfs 탐색
def dfs(r, c):
    # 상/하/좌/우/대각선 확인
    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, -1, 1]

    # 산봉우리인지 체크
    global x

    # 탐색 체크
    visited[r][c] = 1

    # 8가지 방향 탐색
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]

        # 맵 안에 있으면
        if 0<= nr < n and 0<=  nc < m:
            # 주변 산봉우리보다 작으면 False
            if grid[r][c] < grid[nr][nc]:
                x = False
            # 같은 높이의 산봉우리 탐색
            if not visited[nr][nc] and grid[nr][nc] == grid[r][c]:
                dfs(nr, nc)


n, m = map(int,input().split())
# 2차원 그래프를 표현
grid = [list(map(int,input().split())) for _ in range(n)]
# 탐색 여부
visited = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        # 산봉우리가 0보다 크고 탐색하지 않았다면
        if grid[i][j] > 0 and not visited[i][j]:
            x = 1
            dfs(i, j)

            # 산봉우리이면 카운트
            if x:
                cnt += 1
                print(i,j)

print(cnt)