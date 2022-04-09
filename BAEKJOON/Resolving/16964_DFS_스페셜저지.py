N = int(input())
grid = [[0]*(N+1) for _ in range(N+1)]

for i in range(N-1) :
    a,b = map(int,input().split())
    grid[a][b] = 1

ans = list(map(int,input().split()))

