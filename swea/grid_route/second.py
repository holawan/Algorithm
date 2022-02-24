def dfs(x) :
    visted[x] = 1 
    for i in range(1,V+1) :
        if grid[x][i] == 1 and not visted[i]:
            dfs(i)

T = int(input())
for t in range(1,T+1) :
    V,E = map(int,input().split())

    grid = [[0]*(V+1) for _ in range(V+1)] 

    lst = []
    for _ in range(E) :
        lst.append(list(map(int,input().split())))
    S,G = map(int,input().split())
    visted = [0]*(V+1)

    for node in lst :
        grid[node[0]][node[1]] = 1 

    dfs(S)

    if visted[G] == 1 :
        print(f'#{t} 1')
    else :
        print(f'#{t} 0')