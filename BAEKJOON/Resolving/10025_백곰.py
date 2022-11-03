import sys 

input =sys.stdin.readline
n,k =map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

ice = [0]*1000001

for i in range(n) :
    ice[grid[i][1]] = grid[i][0]


next = 2*k + 1 

window = sum(ice[:next])

answer = window 

for i in range(next,1000001) :
    window += (ice[i]-ice[i-next])

    answer = max(answer,window)
print(answer)