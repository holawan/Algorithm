x,y = map(int,input().split())
num = int(input())
stores = [list(map(int,input().split())) for i in range(num+1)] #상근이까지 


for store in stores : 
    if store[0] == 1 :
        store[0] = store[1]
        store[1] = y

    elif store[0] == 2:
        store[0] = store[1]
        store[1] = 0

    elif store[0] == 3 :
        store[0] = 0
        store[1] = y-store[1]

    else :
        store[0] = x
        store[1] = y-store[1]
    
s = stores[-1]
stores = stores[:-1]

cnt = 0
for store in stores :

    if s[0] == 0 :
        direction = 1
    else :
        direction = 0

    sangx,sangy = s[0],s[1]
    sol1=sol2=0

    #시계 
    dy = [0,1,0,-1]
    dx = [-1,0,1,0] 

    if s[0] == 0 :
        direction = 1
    elif s[0] == x:
        direction = 3
    elif s[1] == 0 :
        direction = 0
    else :
        direction = 2

    while [sangx,sangy] != store :
        sangx += dx[direction]
        sangy += dy[direction] 
        if sangx<0 or sangy<0 or sangx>x or sangy>y :
            sangx -= dx[direction]
            sangy -= dy[direction] 
            direction = (direction+1)%4
            sangx += dx[direction]
            sangy += dy[direction] 
        sol1 +=1 

    #반시계
    dy = [0,1,0,-1]
    dx = [1,0,-1,0] 

    if s[0] == 0 :
        direction = 3
    elif s[0] == x:
        direction = 1
    elif s[1] == 0 :
        direction = 0
    else :
        direction = 2
    sangx,sangy = s[0],s[1]

    while [sangx,sangy] != store :
        sangx += dx[direction]
        sangy += dy[direction] 
        if sangx<0 or sangy<0 or sangx>x or sangy>y :
            sangx -= dx[direction]
            sangy -= dy[direction] 
            direction = (direction+1)%4
            sangx += dx[direction]
            sangy += dy[direction] 
        sol2 +=1 
    cnt += min(sol1,sol2)
print(cnt)