T = int(input())

for t in range(1,T+1) :

    lst = [list(input()) for _ in range(5) ]

    l_max = len(max(lst,key=len))

    grid =[[-1]*l_max for _ in range(5)]

    for i in range(len(lst)):
        for j in range(len(lst[i])) :
            grid[i][j] = lst[i][j]


    result = ''
    for i in range(len(grid)) :
        for j in range(len(grid)):
           if grid[j][i] == -1 :
               continue
           else :
               result += grid[j][i]
    print(f'#{t} {result}')