T = int(input())

for t in range(1,T+1) :
    n = int(input())
    lst = list(map(int,input().split()))

    res = []
    for i in range(n-1) :
        for k in range(i+1,n):
            num_times = lst[i]*lst[k]
            for j in range(len(str(num_times))-1):
                if int(str(num_times)[j])>int(str(num_times)[j+1]) :
                    break
            else :
                res.append(num_times)
    if res == [] :
        result = -1
    else :
        result = max(res)
    print(f'#{t} {result}')
