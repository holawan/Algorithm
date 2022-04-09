from itertools import combinations


N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]
sum_grid = [[0]*N for _ in range(N)]
l = set(range(0,N))
l1 = set(combinations(l,N//2))
l3 = []
min_result = 10e9
for i in l1 :
    l2 = tuple(l-set(i))
    result1 = 0
    result2 = 0 

    for j in range(len(i)-1) :
        for k in range(j+1,len(i)) :
            result1 += grid[i[j]][i[k]] + grid[i[k]][i[j]]
            result2 += grid[l2[j]][l2[k]] + grid[l2[k]][l2[j]]


    if abs(result1-result2) < min_result :
        min_result = abs(result1-result2)

print(min_result)
