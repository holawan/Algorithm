T = int(input())
for t in range(1,T+1) :
    n = int(input())
    lst = list(map(int,input().split()))
    for i in range(n,-1,-1) : #버블솔트
        for j in range(0,i-1) :
            if lst[j] > lst[j+1] :
                lst[j],lst[j+1] = lst[j+1],lst[j]
    result = [0]*10 # result 값 만들기

    for i in range(10) : #10개만큼 돌면서
        if i%2 : #i가 홀수이면
            result[i] = lst[i//2] #result[i]는 lst에서 i를 2로 나눈 몫
        else :
            result[i] = lst[-(i//2+1)] #짝수이면 i를 2로 나눈 몫 +1에 마이너스 씌움


    print(f'#{t}', end = ' ')
    print(*result)