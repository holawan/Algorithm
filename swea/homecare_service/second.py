import sys 
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1) : 
    N,M = map(int,input().split())

    grid=  [list(map(int,input().split())) for _ in range(N)]

    homelst = []
    for i in range(N) :
        for j in range(N) :
            if grid[i][j] :
                homelst.append([i,j])
    ans = 0
    max_K = N 
    for k in range(1,max_K + 2 ) :
        for i in range(N) :
            for j in range(N) :
                home = 0
                for hr,hc in homelst :
                    if abs(i-hr)+abs(j-hc) <k :
                        home += 1 
                if k**2+(k-1)**2 < home*M and home>ans :
                    ans = home
    print(f'#{t} {ans}')

