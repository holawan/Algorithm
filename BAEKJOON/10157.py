C, R = map(int,input().split())

board = [[0 for j in range(C)] for i in range(R)] 
from pprint import pprint
pprint(board)

C = C-1 ; R = R

for i in range(1,R*C+1) :
    if i < C :
        board[C-i-2][0] = i
    elif i < C+R :
        board[0][i-R-1] = 
    elif i < 2*C+R-1 :
        board[i+1-2*C][C] = i
    pass

pprint(board)