import sys
n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
lst.sort()

lst2 = [0]
for i in range(len(lst)) :
    x = 1
    ax = lst[i][1]
    if len(lst)-i+1 <= max(lst2) :
        break
    for j in range(i+1,len(lst)) :
        if ax <= lst[j][0] :
            x += 1
            ax = lst[j][1]
    lst2.append(x)
print(max(lst2))