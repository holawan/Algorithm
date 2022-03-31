T = int(input())


def func(r,n,ans) : 
    #최종 결과 글로벌 
    global res

    #현재까지 더한값이 결과보다크면 리턴 
    if ans>res :
        return
    #마지막 행을 지났을 때 비교하고 리턴 
    if r == n :
        if ans<res :
            res = ans 
        return 
    for c in range(n) :
        if not visited[c]  :
            new = grid[r][c]
            visited[c] = 1
            func(r+1,n,ans+new)
            visited[c] = 0 
            




for t in range(1,T+1) : 
    n = int(input())
    #그리드 만들기 
    grid = [list(map(int,input().split())) for _ in range(n)]
    #같은 열 방문 방지하도록 방문 배열 
    visited = [0]*(n+1)
    #초기 정답 
    res = 10e9
    #함수 돌리기 
    func(0,n,0)
    print(f'#{t} {res}')