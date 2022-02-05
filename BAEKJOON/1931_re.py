import sys
n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
lst.sort()
dic = {}
for i in range(n-1,0,-1) :
    dic[lst[i][0]] = lst[i][1]

lst = sorted(list(dic.keys()))


for i in lst :
    pass