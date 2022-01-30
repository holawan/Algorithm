from itertools import count


lst = [] 
for i in range(3) :
    lst.append(int(input()))
x = str(lst[0]*lst[1]*lst[2])

for i in range(10) :
    print(x.count(str(i)))