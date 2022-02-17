import sys

sys.stdin = open('input_2.txt', 'r')
for i in range(10):
    t = int(input())
    grid = [list(map(int, input().split())) for i in range(100)]

    # y = 99  # 가장 아래 시작점 x축
    # x = grid[-1].index(2)  # 시작점 y축
    min_cnt = 1000000
    for i in range(100) :
        if grid[0][i] == 1 : #0행 i열이 1인 경우에만 시작
            x = i # x = i
            y = 0 # y는 0
            cnt = 0 #움직인 횟수를 셀 cnt 0으로 초기화
        else :
            continue
        while y < 99:  # 99가 될때까지
            if 0 < x <= 99 and grid[y][x - 1] == 1:  # x가 index 범위 내에 있으면서 현 위치의 왼쪽이 1이면
                while x != 0 and grid[y][x - 1] == 1:  # x가 0이 아니면서 왼쪽이 1이면 x가 0이거나 왼쪽이 1이 아닐때까지 x축으로 -1
                    x -= 1
                    cnt +=1 #x축으로 움직인만큼 cnt도 추가
                y += 1 #while문 연산이 끝나면 y축으로 한 칸 내려감
                cnt += 1# cnt도 추가
            elif 0 <= x < 99 and grid[y][x + 1] == 1:  # x가 index 범위 내에 있으면서
                while x != 99 and grid[y][x + 1] == 1:  # x가 99가 아니면서 오른쪽이 1이면 x가 99이거나 오른쪽이 1일 때까지 x축으로 +1
                    x += 1#
                    cnt +=1  #x축으로 움직인만큼 cnt도 추가
                y += 1  #while문 연산이 끝나면 y축으로 한 칸 내려감
                cnt +=1 # cnt도 추가
            else:
                y += 1 #좌우가 1이 아니면 그냥 아래로 내려감
                cnt +=1 # 이동횟수 추가
        if cnt <= min_cnt : #이동횟수가 이전 이동횟수보다 작으면
            min_cnt = cnt   #최소 이동 횟수 갱신
            min_idx = i     #return 할 idx갱신
    print(f'#{t} {min_idx}')


