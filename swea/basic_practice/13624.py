T = int(input())                    #테스트 케이스
for t in range(1, T + 1):           #출력값을 맞추기 위해 1부터
    N = int(input())                #카드의 수
    num = list(map(int, input()))   #카드를 리스트로 받기

    c = [0] * 10                    #카운트리스트 만들기
    for n in range(len(num)):       #숫자를 돌며
        c[num[n]] += 1              #카운트의 인덱스와 일치하면 카운트 리스트 인덱스에 +1

    my_max = c[0]                    #초기 최대값은 숫자 0의 개수
    idx = 0                         #초기 인덱스는 0
    for i in range(1, 10):          #카운트 리스트를 순회하며
        if c[i] >= my_max:          #c[i]가 my_max보다 클 경우
            my_max = c[i]           #my_max를 c[i]로 변경 * 카운트가 더 크면 더 큰수가 출력되기 위해 my_max 이상으로 선언
            idx = i                 #인덱스 갱신

    print(f'#{t} {idx} {my_max}')

#! TIP : my_max를 적용하지 않고, c[idx]해도 답이 나올듯 !!