N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)] 


grid = [[0]*1001 for i in range(1001)]



for k in range(len(lst)) :
    for i in range(lst[k][0],lst[k][0]+lst[k][2]) :
        for j in range(lst[k][1],lst[k][1]+lst[k][3]) :
            grid[i][j] = k+1


for k in range(1,N+1) :
    cnt = 0
    for m in grid :
        cnt += m.count(k)
    print(cnt)



