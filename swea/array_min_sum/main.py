import sys 

sys.stdin = open('input.txt','r')


def dfs(n,i) :
    tmp = grid[n][i]
    if 0<=n+1<N :
        dfs(n+1,i)

    



T = int(input())

N = int(input())

grid = [list(int(input()).split()) for _ in range(n)]
cnt = 1 
tmp = 0 
for i in range(N) :
    dfs(0,i)