import sys
n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
lst.sort(key=lambda x:x[0])
lst.sort(key = lambda x:x[1])

cnt = 1
conference = lst[0][1] 
for i in range(1,n) :
    if lst[i][0] >= conference:
        cnt +=1
        conference = lst[i][1]
print(cnt)