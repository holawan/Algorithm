
T = int(input())


def DFS(x,ssum) :
    global ans 

    if ssum>= b+ans :
        return 

    if x==n :
        if ssum >= b and ans>ssum-b :
            ans = ssum-b 
        return
    
    DFS(x+1, ssum+lst[x]) #숫자를 포함하는 경우
    DFS(x+1,ssum)



for t in range(1,T+1): 
    n,b = map(int,input().split())
    lst = list(map(int,input().split()))
    ans = 10e5
    DFS(0,0)
    print(f'#{t} {ans}')