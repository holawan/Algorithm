import sys
sys.stdin = open('input.txt','r')

T = input()

d,w,k = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(d)]

res = 0
ans = 0
x = 0
def func(d,w,k) :
    global ans
    x = 0
    for i in range(w-k) :
        for j in range(d) :
            tmp = 0
            for x in range(k) :
                tmp += grid[i][j]
            if tmp == 0 or tmp == k :
                ans = 0
                break
            else :
                x = -1
        if x == -1 :
            break
    if
print(func(d,w,k))





