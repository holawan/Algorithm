import sys
sys.stdin = open('input_03.txt','r')
for test in range(10) :
    #데이터 불러오기
    t = int(input())
    n = 100
    lst = [list(map(int,input().split())) for _ in range(n)]
    #결과의 초기값 0
    result = 0
    cross_sum = 0
    cross_sum2 = 0
    for i in range(n) :
        #행별 계산 후 최대값 갱신
        if sum(lst[i]) > result :
            result = sum(lst[i])
        new_sum =0
        for j in range(n) :
            #열별 계산 후 최대값 갱신
            new_sum += lst[j][i]
        # 대각선 계산 후 갱신
        if new_sum >result :
            result = new_sum
        cross_sum += lst[i][i]
        if cross_sum > result:
            result = cross_sum
        cross_sum2 += lst[-i - 1][i]
        if cross_sum > result:
            result = cross_sum

    print(f'#{test+1} {result}')