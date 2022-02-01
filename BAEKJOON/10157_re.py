C,R = map(int,input().split())
board = [[0 for j in range(C)] for i in range(R)] 

for i in range(R,0,-1) :
    for j in range(C-1,0,-1) :
