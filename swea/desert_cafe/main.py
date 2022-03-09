import sys


sys.stdin = open('input.txt','r')

T = int(input())

n = int(input())

grid = [list(map(int,input().split()))for _ in range(n)]

dr = [1,1,-1]
dc = [1,-1,-1]
res = []
for i in range(n):
    for j in range(n) :
        for num in range(1,n-1) :
            tmp_lst = [grid[i][j]]
            new_i = i; new_j = j
            for k in range(3) :
                new_i += dr[k]
                new_j += dc[k]
                if 0<=new_i<n and 0<=new_j<n and not(grid[new_i][new_j] in tmp_lst) :
                    tmp_lst.append(grid[new_i][new_j])
                else :
                    break
            else :
                print(tmp_lst)
                res.append(len(tmp_lst))
print(res)