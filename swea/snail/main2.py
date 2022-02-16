#테스트 케이스 불러오기
T = int(input())

for t in range(1,T+1) :
    n = int(input())
    #그리드 만들기
    grid = [[0]*n for _ in range(n)]
    #숫자가 움직이는 방향 우,하,좌,상
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    #초기값 설정
    direction = i = j= 0
    # 끝날때까지
    for num in range(1,n**2+1) :
        #그리드에 숫자 추가
        grid[i][j] = num
        #방향에 따라 해당 축에 +=1
        i += dy[direction]
        j += dx[direction]

        #범위를 벗어나거나 해당 자리에 이미 값이 있으면
        if i <0 or j < 0 or i >= n or j >=n or grid[i][j]:
            #방향 전환
            i -= dy[direction]
            j -= dx[direction]
            if direction < 3 :
                direction +=1
            else :
                direction -=3
            i += dy[direction]
            j += dx[direction]

    print(f'#{t}')

    for i in grid:
        print(*i)




