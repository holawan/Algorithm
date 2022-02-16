T = int(input())
for t in range(1,T+1) :
    #테스트 케이스를 순회하며 집합 받기
    lst = list(map(int,input().split()))
    n = len(lst)
    #결과를 반환할 x
    x = 0
    #공집합을 제외하고 1부터 2의 n승까지
    for i in range(1,1<<n) :
        tmp_set = []
        for j in range(n):
            if i & (1<<j) :
                tmp_set.append(lst[j])
        if sum(tmp_set) == 0 :
            x = 1
            break

    if x== 1 :
        print(f'#{t} {x}')
    else :
        print(f'#{t} {x}')