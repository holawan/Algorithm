import heapq

N = int(input())

work = [list(map(int,input().split())) for _ in range(N)]

work.sort(key=lambda x:(x[0],x[1]))
heap = []
heapq.heappush(heap, work[0][1])

for i in range(1,N) :
    # 다음 수업 시작 시간이 현재 강의실 수업 시작의 최소값보다 작으면 
    #강의실 추가 사용 
    if work[i][0] < heap[0] :
        heapq.heappush(heap,work[i][1])
    #다음 수업시작시간이 현재 강의실 수업시작의 최소값보다 크거나 같으면 강의실 이어사 사용 
    else :
        heapq.heappop(heap)
        heapq.heappush(heap,work[i][1])
print(len(heap))