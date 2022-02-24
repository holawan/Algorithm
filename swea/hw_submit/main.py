T = int(input())
for t in range(1,T+1) :
    n,submit = map(int,input().split())
    submit_stu = list(map(int,input().split()))
    student = list(i for i in range(1,n+1))
    res = []
    for i in student :
        if i in submit_stu :
            continue
        else :
           res.append(i)
    print(f'#{t}',end=' ')
    res.sort()
    print(*res)