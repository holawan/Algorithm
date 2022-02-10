T = int(input())        #테스트 케이스 수
for r in range(1,T+1) : #출력 형식을 맞추기 위한 1부터 시작
    n = int(input())    #숫자의 수 불러오기
    num = list(map(int,input().split())) #숫자를 리스트로 받기

    my_max = num[0]         #최대값 초기값은 첫번째 값
    my_min = num[0]         #최소값 초기값은 첫번째값
    for i in range(1,n) :   #숫자 리스트를 순회하며
        if num[i] > my_max :#숫자가 my_max보다 크면 갱신
            my_max = num[i]
        if num[i] < my_min: #숫자가 my_min보다 작으면 갱신
            my_min = num[i]
    print(f'#{r} {my_max-my_min}')