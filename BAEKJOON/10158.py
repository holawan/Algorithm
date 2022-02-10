import sys

w, h = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

lst = [0,0,w,h] 

dx,dy = 'p','p'
for i in range(t) :

    if (x==w and y==h) or y==h:
        dx,dy='m','m'
    elif (x==0 and y==0) or x==0:
        dx,dy = 'p','p'
    elif x== w  or y==0:
        dx,dy = 'm','p'
    if dx == 'p':
        x+=1
    else :
        x-=1
    if dy == 'p':
        y+=1
    else : 
        y-=1
print(x,y)