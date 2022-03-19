import sys 
sys.stdin = open('input.txt','r')


def dfs(n, alst, blst) :
    global ans 
    if n== N :
        if len(alst) == len(blst) :
            asum = bsum = 0 
            for i in range(len(alst)) :
                for j in range(len(alst)) :
                    asum += grid[alst[i]][alst[j]]
                    bsum += grid[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return 
    
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])


T = int(input())
for t in range(1,2) :
    N = int(input())
    grid=  [list(map(int,input().split())) for _ in range(N)]
    ans = 10000 
    dfs(0,[],[])
    print(f'#{t} {ans}')


