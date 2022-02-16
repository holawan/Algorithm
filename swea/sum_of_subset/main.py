T = int(input())
for t in range(1,T+1) :
    n , k = map(int,input().split())
    A = [i+1 for i in range(12)]

    cnt = 0

    #부분집합의 모든 경우를 돌면서
    for i in range(1<<12) :
        #공집합일 경우부터 모든 원소를 부분집합으로 가지는 집합까지
        #빈 셋에
        tmp_set = []
        for j in range(12) :
            #i의 j번째 비트가 1인지 아닌지 확인
            if i & (1<<j) :
                #for문을 순회하며 and연산 결과 True이면 A리스트의 j 인덱스를 tmp_set에 추가
                tmp_set.append(A[j])
        # print(tmp_set)
        #크기와 합 비교
        if len(tmp_set)== n and sum(tmp_set) == k :
            cnt +=1
        # if i == 13 :
        #     break
        '''
            []
            [1]
            [2]
            [1, 2]
            [3]
            [1, 3]
            [2, 3]
            [1, 2, 3]
            [4]
            [1, 4]
            [2, 4]
            [1, 2, 4]
            [3, 4]
            [1, 3, 4]
        '''
    print(f'#{t} {cnt}')
