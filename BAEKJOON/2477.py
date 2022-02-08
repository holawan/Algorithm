n = int(input())

#w = 1,2 h = 3,4

lst=[]
wlst=[]
hlst=[]
for i in range(6) :
    a,b = map(int,input().split())
    if a == 1 or a== 2 :
        wlst.append(b)
        lst.append(b)
    else :
        hlst.append(b)
        lst.append(b)
W = max(wlst)
H = max(hlst)

L_square = W*H



x1 = lst[lst.index(W)+1 if lst.index(W)==5 else lst.index(W)-5]
x2 = lst[lst.index(W)-1]

y1 = lst[lst.index(H)+1 if lst.index(W)!=5 else lst.index(W)-5]
y2 = lst[lst.index(H)-1]

s_square=abs(x1-x2)*abs(y1-y2)


print((L_square-s_square)*n)