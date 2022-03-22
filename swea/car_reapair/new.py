import sys 
sys.stdin = open('input.txt','r')


#지갑을 두고 간 고객과 같은 접수창구A와 같은 정비창구 B를 이용한 고객들의 고객번호 합 

T = int(input())

for tc in range(1,3) : 
    #N = 접수창구 개수, M = 정비 창구 개수, K = 고객 수, A =target의 접수, B = target의 정비
    N, M, K, A , B = map(int,input().split())

    #i번째 접수창구가 고장을 접수하는데 걸리는 시간  -> N개 
    a = list(map(int,input().split()))
    #j번째 정비 창구가 차량을 정비하는데 걸리는 시간 -> M개 
    b = list(map(int,input().split()))
    #고객이 차량정비소를 방문하는 시간 t -> K개
    t = list(map(int,input().split()))

    print(N,M,K,A,B,a,b,t)


    t_idx = 0
    len_t = len(t)


    #방문기록 저장 
    visitor_info = [[-1,-1] for _ in range(K)]

    #접수창구 배열
    reception_desks = [-1] * N 
    #정비창구 배열 
    repair_desks = [-1] * M 

    #접수 대기줄 
    reception_wating_line = []
    #정비 대기줄 
    repair_wating_line = []
    time = 0

    while True :
        #정비가 끝났으면 끝
        for i in range(M) :
            if repair_desks[i] != -1 and repair_desks[i][1] == 0 :
                repair_desks[i] = -1
        # 접수창구에서 나오면 정비창구대기열로 
        for i in range(N) :
            if reception_desks[i] != -1 and reception_desks[i][1] == 0 :
                repair_wating_line.append(reception_desks[i][0])
                reception_desks[i] = -1 
        #방문한 고객을 접수창구 대기열로
        for i in range(t_idx,len_t) :
            if t[i] == time :
                reception_wating_line.append(i) 
            else :
                t_idx = i 
                break
        #정비창구 비어있는 곳에 대기열 사람 옮기기 
        for i in range(M) :
            if repair_desks[i] == -1 and repair_wating_line :
                visitor_idx = repair_wating_line.pop(0)
                repair_desks[i] = [visitor_idx,b[i]-1]
                #몇 번 정비 창구 방문했는지 기록
                visitor_info[visitor_idx][1] = i
            elif repair_desks[i] != -1 :
                repair_desks[i][1] -= 1 
        
        #접수창구 비어있는 곳에 대기열 사람 옮기기
        for i in range(N) :
            if reception_desks[i] == -1 and reception_wating_line:
                visitor_idx = reception_wating_line.pop(0)
                reception_desks[i] = [visitor_idx,a[i]-1]
                #몇 번 접수창구 방문했는지 기록
                visitor_info[visitor_idx][0] = i 
            elif reception_desks[i] != -1 :
                reception_desks[i][1] -= 1 
        
        #모든 창구 사람 남은시간 -1 하기 위, 3, 4 에서 함께 처리

        time+= 1 
        if time>K :
            for i in range(K) :
                if visitor_info[i][1] == -1 :
                    break
            else :
                break
        
    ans = 0

    for i in range(K) :
        if visitor_info[i][0] == A-1 and visitor_info[i][1] == B-1 :
            ans += i + 1 
    if ans == 0:
        ans = -1 
    
    print(f'#{tc} {ans}')