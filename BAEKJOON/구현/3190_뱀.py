from collections import deque

#보드의 크기 
n = int(input())
#그리드 만들기 
grid = [[0]*n for _ in range(n)]
#사과의 수 
apple = int(input())

#사과 배치하기 
for _ in range(apple) :
    r,c = map(int,input().split())
    grid[r-1][c-1] = 1
#방향전환 
l = int(input())
#딕셔너리 형태로 만들기 
change = {}
for _ in range(l) :
    x,y = input().split()
    change[int(x)] = y


#방향 
dr = [0,1,0,-1]
dc = [1,0,-1,0]
#초기방향 오른쪽 
d = 0

time = 0
#뱀 넣기 
snake = deque([(0,0)])

while True :
    # print(snake)
    #방향전환을 해야하면 
    if time in change.keys() :
        #왼쪽 오른쪽에 따라 방향전환하기 
        if change[time] == 'L' :
            d -=1 
            if d<0 :
                d = 3
        else :
            d = (d+1)%4
    #뱀꺼내서 
    cr,cc = snake.popleft()
    #이동시킨다. 
    nr,nc = cr + dr[d] ,cc + dc[d]

    # print(nr,nc)
    #범위를 벗어나거나 자기와 부딪히면 멈추기 
    if nr>=n or nr<0 or nc>=n or nc<0 or (nr,nc) in snake :
        break
    #사과가 있다면 
    elif grid[nr][nc] :
        #사과를 없애고 
        grid[nr][nc] = 0
        #현위치 맨 앞에 추가 
        snake.appendleft((cr,cc))
        #몸 한칸 늘려서 맨 앞에 추가 
        snake.appendleft((nr,nc))
        #빈곳이라면 
    elif grid[nr][nc] == 0 :
        #현위치 맨 앞에 추가 
        snake.appendleft((cr,cc))
        #몸 한 칸 늘려서 맨 앞에 추가 
        snake.appendleft((nr,nc))
        #꼬리 뒤에 없애기 
        snake.pop()

    time += 1

print(time+1)