import pprint
a,b = map(int,input().split()) 
num = int(input())
lst = [list(map(int, input().split())) for _ in range(num)] 
for decision in lst :
    if decision[0] == 1 :
        a += 1 
    else : 
        b += 1 

board = [[0 for j in range(b)] for i in range(a)] # 그리드 만들기

for decision in lst :
    if decision[0] == 0 :
        for i in range(b) :
            board[decision[1]][i] = 1 
    else :
        for i in range(a) :
            board[i][decision[1]] = 1
pprint.pprint(board)
