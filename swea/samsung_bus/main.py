T = int(input())

for t in range(1,T+1) :
    N = int(input())

    lst_route = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    stop_lst = [int(input()) for _ in range(P)]

    result = [0]*P

    for stop in range(P) :
        for j in lst_route :
            if j[0]<= stop_lst[stop] <= j[1] :
                result[stop] +=1
    print(f'#{t}',end=" ")
    print(*result)