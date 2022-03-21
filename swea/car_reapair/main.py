import sys 
sys.stdin = open('input.txt','r')


#지갑을 두고 간 고객과 같은 접수창구A와 같은 정비창구 B를 이용한 고객들의 고객번호 합 

T = int(input())

#N = 접수창구 개수, M = 정비 창구 개수, K = 고객 수, A =target의 접수, B = target의 정비
N, M, K, A , B = map(int,input().split())

#i번째 접수창구가 고장을 접수하는데 걸리는 시간  -> N개 
a = list(map(int,input().split()))
#j번째 정비 창구가 차량을 정비하는데 걸리는 시간 -> M개 
b = list(map(int,input().split()))
#고객이 차량정비소를 방문하는 시간 t -> K개
t = list(map(int,input().split()))
#고객 접수 번호
receipt_num = [[i] for i in range(1,K+1)]
#시간
times = [[i] for i in range(max(t))]
#접수 방문표시
visited_N = [[0] for _ in range(N)]
#정비 방문표시
visited_M = [[0] for _ in range(M)]
from collections import deque
wait_N = deque([])
wait_M = deque([])

def receipt(receipt_num) :
    if 0 in visited_N :
        for search in range(N) :
            if visited_N[search] == 0 :
                visited_N[search] = receipt_num + n[search]
                break
    else : 
        wait_N.append(receipt_num)


def fix(out_time,wait_time) :
    if 0 in visited_M :
        for search in range(M) :
            if visited_M[search] == 0 :
                visited_N[search] = out_time + m[search]
                break
    else : 
        wait_M.append(out_time,wait_time)

for time in times :
    for j in range(len(t)) :
        if time == t[j] :
            receipt(receipt_num)
        elif time> t[j] :
            break
    
