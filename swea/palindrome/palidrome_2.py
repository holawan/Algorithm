
def func(grid) :
    grid2 = list(map(list, zip(*grid)))
    for m in range(100,0,-1) :
        for row in range(100) :
            for column in range(100-m+1) :
                if grid[row][column:column+m] == grid[row][column:column+m][::-1] :
                    return m
                elif grid2[row][column:column+m] == grid2[row][column:column+m][::-1] :
                    return m

import sys
sys.stdin = open('input.txt','r')

for t in range(10) :
    T = int(input())
    grid = [list(input()) for _ in range(100)]
    print(f'#{T} {func(grid)}')
