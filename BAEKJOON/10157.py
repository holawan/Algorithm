C, R = map(int,input().split())

board = [[0 for j in range(C)] for i in range(R)] 
from pprint import pprint
pprint(board)
n= int(input())

lst=[i for i in range(1,C*R+1)]

lst2 = []
for i in lst :
    if i<R :
        lst2.append([1,i])
    elif i<C+R-1 :
        lst2.append([i-C+2,R])
    elif i<2*(R)- C-1 :
        lst2.append()
print(lst2)