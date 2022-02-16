import sys
sys.stdin = open('input.txt','r')
T = int(input())
for t in range(1,T+1) :
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    dx = [0,0,-1,1] #좌우
    dy = [1,-1,0,0] #상하

    result = 0 #결과 초기값

    for i in range(n) : #테스트 케이스 행
        for j in range(n) : #테스트 케이스 열
            x = 0 #초기 이웃합 0
            for d in range(4) : #상하좌우를 돌며
                if 0<=i+dx[d]<n  and 0<=j+dy[d] <n: #현위치에서 각 상하좌우 값을 더할 때 행렬 범위 내에 있으면
                    x += abs(lst[i][j]-lst[i+dx[d]][j+dy[d]]) #이웃합에 현위치 값 - 이웃의 절대값을 더함
            result += x
    print(f'#{t} {result}')