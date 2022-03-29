import sys 
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1) :
    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]

    #시작시간 우선 정렬 시작시간이 같으면 종료시간 역 정렬 
    lst.sort(key=lambda x:(x[0],-x[1]))
    print(lst)
    cnt = 1 
    #시작지점은 마지막 지점의 출발시간 
    end = lst[-1][0]
    print(lst)
    #뒤에서부터 돌면서 
    for i in range(N-2,-1,-1) :
        if lst[i][1] <=end : #도착시간이 현재 출발시간보다 작거나 같으면 
            cnt += 1 
            end = lst[i][0] #해당 인덱스의 출발시간을 끝지점으로 설정 
        
    print(f'#{t} {cnt}')
