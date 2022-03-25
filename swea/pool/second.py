import sys 
sys.stdin = open('input.txt','r')

T = int(input())


def dfs(n,ssum) :
    global ans 
    if n >12 :
        if ans >ssum :
            ans = ssum
        return
    dfs(n+1,ssum+plan[n]*pay[0])
    dfs(n+1,ssum+pay[1])
    dfs(n+3,ssum+pay[2])    


for t in range(1,T+1) :
    pay = list(map(int,input().split()))
    plan = [0]+list(map(int,input().split()))

    ans = pay[3] 
    dfs(1,0)
    print(f'#{t} {ans}')

