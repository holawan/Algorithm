import sys

sys.stdin = open('input.txt','r')
for i in range(10) :
    t = int(input())
    grid = [list(map(int,input().split())) for i in range(100)]
    
    y = 99 #가장 아래 시작점 x축
    x = grid[-1].index(2) #시작점 y축
    while y> 0 : #0이 될때까지
        if 0< x <= 99 and grid[y][x-1] == 1 : #x가 index 범위 내에 있으면서 현 위치의 왼쪽이 1이면
            while x!=0 and grid[y][x-1] == 1 : #x가 0이 아니면서 왼쪽이 1이면 x가 0이거나 왼쪽이 1이 아닐때까지 x축으로 -1
                x -= 1
            y -= 1             #while문 연산이 끝나면 y축을 한 칸 올려준다.
        elif 0<= x <99 and grid[y][x+1] == 1 : #x가 index 범위 내에 있으면서
            while x!=99 and grid[y][x+1] == 1  :#x가 99가 아니면서 오른쪽이 1이면 x가 99이거나 오른쪽이 1일 때까지 x축으로 +1
                x += 1
            y-=1                #while문 연산이 끝나면 y축을 한 칸 올려준다.
        else :
            y -=1               #둘다 아니면 그냥 위로 간다.
    print(f'#{t} {x}')


