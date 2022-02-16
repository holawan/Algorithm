T = int(input())
for t in range(1,T+1) :
    n = int(input())
    lst = list(map(int,input().split()))
    result = [] #결과반환 리스트
    for i in range(10) : #10번째까지
        if i%2 : #2로 나눈 나머지가 0이면
            result.append(min(lst)) #최소값을 result에 추가하고
            lst.remove(min(lst)) #lst에서 제거한다.
        else : #2로 나눈 나머지가 1이면
            result.append(max(lst)) #최대값을 추가하고
            lst.remove(max(lst)) #lst 에서 제거한다.

    print(f'#{t}',end=' ')
    print(*result)