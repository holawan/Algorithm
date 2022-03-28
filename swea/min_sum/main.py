import sys 
sys.stdin = open('input.txt','r')

T = int(input())
#방향은 아래, 오른쪽 
dr = [1,0]
dc = [0,1]

def dfs(r,c,res) :
    global ans 
    #현재 합이 최소합보다 크면 리턴 
    if res>ans :
        return 
    #마지막 위치에 왔을 때 현재합이 최소합보다 작으면 현재합을 최소합으로 
    if r == N-1 and  c == N-1 :
        if res<ans :
            ans = res 
        return 
    #두방향을 돌면서 
    for d in range(2) : 
        #새로운 방향 입력해주고 
        nr = r+dr[d]
        nc = c+dc[d]
        if 0<=nr<N and 0<=nc<N  :
            #결과에 현재 값 더해주고 
            res += grid[nr][nc]
            #dfs돌리고 
            dfs(nr,nc,res)
            #다시 빼줌 
            res -= grid[nr][nc]



for t in range(1,T+1) :
    N = int(input())
    #그리드 만들기 
    grid=[list(map(int,input().split())) for _ in range(N)]
    #결과값 
    ans = 10e5
    #시작점부터 dfs 돌리기 
    dfs(0,0,grid[0][0]) 
    print(f'#{t} {ans}')