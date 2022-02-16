import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1) :
    #n = 행, m = 열
    n,m = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(n)]
    cntlst = [] #행별 열별 구조물의 합을 담을 리스트
    # row = 행
    # column = 열
    for row in range(n) : #행을 돌면서 행별 구조물 길이를 저장
        cnt = 0
        for column in range(m) :
            if grid[row][column] == 1 : #해당 격자가 1이면
                cnt +=1                 #cnt + 1
            else :                      #0인 격자를 만났을 때
                if cnt >1 :           #구조물 길이가 1보다 크면
                    cntlst.append(cnt)#cnt리스트에 저장
                cnt = 0               #cnt 초기화
        cntlst.append(cnt)            #끝나도 저장

    for column in range(m) : #열고정 후 행을 돌면서 열별 구조물 길이를 저장
        cnt = 0
        for row in range(n) :   #위와 같은 방식으로 진행
            if grid[row][column] == 1 :
                cnt +=1
            else :
                if cnt >1 :
                    cntlst.append(cnt)
                cnt = 0
        cntlst.append(cnt)
    print(f'#{t} {max(cntlst)}')

