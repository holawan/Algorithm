n = int(input())
for i in range(n) :
    H,W,N = map(int,input().split())

    lst = list([0]*W for i in range(H))
    from pprint import pprint

    n = 0
    for i in range(1,W+1) :
        for j in range(1,H+1) :
            n += 1
            if n == N :
                print(j*100 + i)
                break
