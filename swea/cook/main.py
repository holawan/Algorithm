import sys 
sys.stdin = open('input.txt','r')

def dfs(n, alst, blst):
    global ans
    print(n)
    print(f'alst : {alst}')
    print(f'blst : {blst}')
    if n ==N:
        if len(alst) == len(blst):
            asum = 0
            bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += lst[alst[i]][alst[j]]
                    bsum += lst[blst[i]][blst[j]]
 
 
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])
    return ans
TC = int(input())
for tc in range(1, 4):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    alst = []
    blst = []
    ans = 10e5
    print('#{} {}'.format(tc, dfs(0, alst, blst)))