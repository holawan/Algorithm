import sys 
sys.stdin = open('input.txt','r')

T = int(input())

def f(n,k) :
    if n==k :
        #순열리스트에 넣기 
        part.append(p[:])
    else :
        #k만큼 돌면서 
        for i in range(k) :
            if used[i] == 0 : #앞에서 사용하지 않은 숫자인 경우 
                used[i] = 1   # 사용함으로 표시 
                p[n] = lst[i] #p[n]에 숫자 넣기 
                f(n+1,k)      #재귀 
                used[i] = 0   #lst[i]를 다른 위치에서 사용할 수 있도록 함 

for t in range(1,T+1) :
    N = int(input())

    grid = [list(map(int,input().split())) for _ in range(N)]
    
    #시작점을 제외하고 순열 만들기 
    #순열 후보들 
    lst = list(range(1,N))
    #값을 넣을 리스트 
    p = [0]*(N-1)
    #사용 여부
    used = [0]*(N-1)
    #순열들을 넣을 리스트 
    part = []
    #순열 만들기 
    f(0,N-1)

    #사용 값 
    ans = 1e9 
    #순열을 돌면서 
    for i in range(len(part)) :
        #전력 사용량 
        res = 0 
        #순열의 앞뒤를 계산해야하므로 파트의 -1만큼 돌면서 
        for j in range(len(part[i])-1) :
            #방을 돌면서 전력 사용량 더해주기 
            res += grid[part[i][j]][part[i][j+1]]
        #사무실에서 첫번째 방 더하기 
        res += grid[0][part[i][0]]
        #마지막 방에서 사무실 더하기 
        res += grid[part[i][-1]][0]
        #최소 전력량 구하기 
        if res <ans :
            ans =res 

    print(f'#{t} {ans}')