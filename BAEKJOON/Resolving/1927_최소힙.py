import heapq 
import sys



N = int(sys.stdin.readline())
lst = []

for _ in range(N) :
    n = int(sys.stdin.readline())
    if n==0 :
        if not lst :
            print(0)
        else :
            print(heapq.heappop(lst))
    else :
        heapq.heappush(lst,n)
