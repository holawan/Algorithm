x,y,x2,y2 = map(int,input().split())



lst = [0,x2,0,y2]
lst2 = []
for l in lst[:2] :
    lst2.append(abs(x-l))
for l in lst[2:] :
    lst2.append(abs(y-l))
print(min(lst2))
