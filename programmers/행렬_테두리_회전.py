rows=columns=6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
answer=  []
i = 0
grid = [[0]*columns for _ in range(rows)]
for r in range(rows) :
    for c in range(columns) :
        i += 1
        grid[r][c] = i
for i in grid :
    print(i)
print('-------------')
for tmp in queries :
    tmp = [tmp[0]-1, tmp[1]-1, tmp[2]-1, tmp[3]-1]

    seed_r = tmp[0]
    seed_c = tmp[1]
    initial = grid[seed_r][seed_c]
    print(initial)
    ran = ((tmp[3]-tmp[1])+(tmp[2]-tmp[0]))*2 
    res = [initial]
    initi = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    i = 0
    while initi<ran :
        seed_r += dy[i] 
        seed_c += dx[i]
        if tmp[0]<=seed_r<=tmp[2] and tmp[1]<=seed_c<=tmp[3] :
            initial2 = grid[seed_r][seed_c]
            grid[seed_r][seed_c] = initial
            initial = initial2
            res.append(initial)
            print(initial)
        else :
            seed_r -= dy[i]
            seed_c -= dx[i]
            i = (i+1)%4
            seed_r += dy[i]
            seed_c += dx[i]
            initial2 = grid[seed_r][seed_c]
            grid[seed_r][seed_c] = initial
            initial = initial2
            res.append(initial)
            print(initial)
        initi += 1 
    for i in grid :
        print(i)
    print('-----------')

    answer.append(min(res))
print(answer)




