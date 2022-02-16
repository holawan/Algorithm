T = int(input())
for t in range(1,T+1) :
    n = int(input())
    red_group = [] #빨간 색을 칠할 그룹
    blue_group = [] #파란색을 칠할 그룹
    for num in range(n): #color정보를 받아서
        color = list(map(int,input().split()))
        if color[-1] == 1 : #마지막 값이 1이면 레드그룹
            red_group.append(color)
        else :              #아니면 블루 그룹
            blue_group.append(color)

    grid = [[0]*10 for i in range(10)] #도화지 만들기

    for red in red_group : #레드그룹을 돌면서
        for i in range(red[0],red[2]+1) : #x축 순회
            for j in range(red[1],red[3]+1) : #y축 순회하며
                if grid[i][j] :
                    continue
                else :
                    grid[i][j] +=1             #1씩 추가
    for blue in blue_group : #블루그룹을 돌면서
        for i in range(blue[0],blue[2]+1) : #x축 순회
            for j in range(blue[1],blue[3]+1) : #y축 순회
                if grid[i][j] :
                    continue
                else :
                    grid[i][j] += 1 #1씩 추가

    cnt = 0 #cnt는 0부터
    for i in range(10) : #도화지를 돌면서
        for j in range(10) :
            if grid[i][j] == 2 : #값이 2이면 색이 두번 칠해졌기 때문에
                cnt +=1 #cnt +=1
    print(f'#{t} {cnt}')
