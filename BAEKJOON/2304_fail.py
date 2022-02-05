n = int(input())
lst = []
M = 0
for i in range(n) :
    a,b = map(int,input().split())
    if b>M :
        M = b 
    lst.append([a,b])
lst.sort()

area = 0
x,y = lst[0][0],lst[0][1]
z = 0
for a,b in lst:
    if b == M:
        z +=1

for i in range(1,n) :
    if lst[i][1]> y :
        area += (lst[i][0]-x)*y 
        x,y = lst[i][0],lst[i][1]
    if lst[i][1] == M :
        idx = i
        area += (lst[i][1])*z
        break


x,y = lst[-1][0],lst[-1][1]

for j in range(n-1,idx-1,-1) :
    if lst[j][1] > y :
        area += (x-lst[j][0])*y
        x,y = lst[j][0],lst[j][1]
    if lst[j][1] == M :
        break

print(area)
    