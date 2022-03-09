import sys


sys.stdin = open('input.txt','r')


T = int(input())
for t in range(1,T+1):
    #일,월,분기, 연별 가격표
    cost = list(map(int,input().split()))
    #월별 이용횟수
    lst = list(map(int,input().split()))

    #1일권만 할 때, 월권으로 다 할 때 분기권, 연권
    ans = [sum(lst)*cost[0] ,cost[1]*12 ,cost[2]*4 ,cost[3]]

    #분기별 이득을 계산할 임시 저장소
    tmp = 0
    count = 0
    table = []

    #각 월별로 일권을 끊었을 때와 월권을 끊었을 때 더 작은 값을 넣음
    for day in lst :
        table.append(min(day*cost[0],cost[1]))

    #월별 최소 요금을 돌면서
    for _ in range(2) :
        for i,v in enumerate(table) :
            #이용안하면 점프
            if v == 0 :
                continue
            elif count != 0 :
                count -=1
                continue
            else :
                #11월일 때
                if i == 10 :
                    #3개월 이용권이 계산된 11월 12월 이용요금보다 작으면
                    if cost[2] < (table[i] + table[i+1]) :
                        #임시저장소에 3개월 요금을 더함
                        tmp += cost[2]
                    else :
                        #아니면 11+12월 요금을 합한걸 더함
                        tmp += (table[i] + table[i+1])
                    #멈춤
                    break
                    #12월일 때
                elif i == 11 :
                    #12월 요금이 3개월요금보다 비싸면
                    if cost[2] < v :
                        #임시저장소에 3개월 요금을 더함
                        tmp += cost[2]
                    else :
                        #아니면 12월 요금 더함
                        tmp += v
                    #멈춤
                    break

                #만약 분기 이용권이 3달 이용구너 합보다 작으면 임시저장소에 추가
                else :
                    if cost[2] < (table[i]+table[i+1]+table[i+2]) :
                        tmp += cost[2]
                        count = 2
                    else :
                        tmp += v

        ans.append(tmp)
        table.reverse()
        tmp = 0
        count = 0
    print(f'#{t} {min(ans)}')