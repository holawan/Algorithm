N = int(input())
p = [0]+list(map(int,input().split()))
p_sum = sum(p)
grid = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1) :
    l = list(map(int,input().split()))

    for x in range(1,len(l)) :
        grid[i][l[x]] = 1
        grid[l[x]][i] = 1


res = 10e9

def dfs(x,population) :
    global n,res
    if n == N :
        tmp = abs((p_sum-population)-population)
        if tmp<res :
            res = tmp
    for new in range(1,N+1) :
        if grid[x][new] == 1 and not new in visited_a :
            visited_a.append(new)
            dfs(new,population+p[new])
            n+=1
        elif not new in visited_b :
            visited_b.append(new)
            n += 1



for x in range(1,N+1) :
    n = 1
    visited_a = [x]
    visited_b = []
    dfs(x,p[x])
print(res)