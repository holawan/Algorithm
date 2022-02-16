T = int(input())
for t in range(1,T+1) :
    n = int(input())
    #그리드 만들기
    grid = [[0]*n for _ in range(n)]

    #숫자 시작 값 1
    x=1
    #grid에 부여할 값의 범위 갱신을 위한 m과 alpha설정
    m = n
    alpha = i = 0

    while x < n**2 :
        # alpha부터 m-1까지(오른쪽 값 혹은 끝에 닿을 때 까지)
        for j in range(alpha,m) :
            grid[i][j] = x
            x+=1
        # alpha+1부터(이전에 무언가에 부딪혔기 때문) m-1까지(아래 끝에 닿을때까지)
        for i in range(alpha+1,m) :
            grid[i][j] = x
            x +=1
        #m-2부터(m-1까지 갔기 때문) alpha-1까지 (왼쪽 끝에 닿을때까지)
        for j in range(m-2,alpha-1,-1) :
            grid[i][j] = x
            x +=1
        # m-2부터(m-1까지 갔기 때문) alpha까지 (위쪽 값에 닿을때까지)
        for i in range(m-2,alpha,-1) :
            grid[i][j] = x
            x+=1
        #alpha 갱신, 범위 갱신
        alpha += 1
        m-=1
    #n이 홀수이면 가운데 값이 n^2을 넣어줌
    if n%2 :
        grid[n//2][n//2] = n**2
    print(f'#{t}')

    for i in grid:
        print(*i)


