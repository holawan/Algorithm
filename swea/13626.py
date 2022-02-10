T = int(input()) #테스트 케이스
for t in range(1,T+1) : #출력 형식을 맞추기 위해 1부터 시작
    N,M = map(int,input().split()) #숫자의 개수와 구간 입력
    num = list(map(int,input().split())) # 숫자 입력

    sum_num = sum(num[0:M]) #초기 구간 합은 0부터 M까지의 합
    sum_m = sum_M = sum_num #초기 구간 최소값, 최대값은 sum_num
    for i in range(N-M) : #숫자리스트를 숫자개수-구간-1 만큼 순회하며
        sum_num = sum_num - num[i] + num[i+M] #새로운 구간합은 기존 구간합에서 앞에 하나를 제외 , 뒤에 하나를 추가한 것
        if sum_num > sum_M : #현재 구간합이 기존 구간합의 최대값보다 크면
            sum_M = sum_num #최대값 변경
        if sum_num < sum_m : #현재 구간합이 기존 구간합의 최솟값보다 작으면
            sum_m = sum_num #최솟값 변경

    print(f'#{t} {sum_M-sum_m}')