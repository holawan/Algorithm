import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1) :
    N,M = map(int,input().split())
    containers = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    
    #초기 정답 
    ans = 0

    #트럭에 싣기 위해 정렬 
    containers.sort()
    trucks.sort()

    #둘다 존재하면 ㄱ ㄱ 
    while containers and trucks: 
        #트럭 마지막값이 컨테이너 마지막값보다 크거나 같으면 
        if trucks[-1]>= containers[-1] :
            #트럭에 싣고 
            ans += containers[-1]
            #트럭 제거 
            trucks.pop()
        #트럭에 실었거나 컨테이너가 너무 크거나 제거 
        containers.pop()
    print(f'#{t} {ans}')
