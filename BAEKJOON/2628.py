import pprint
a,b = map(int,input().split()) 
num = int(input())
lst = [list(map(int, input().split())) for _ in range(num)] 
for decision in lst :
    if decision[0] == 1 :
        a += 1 
    else : 
        b += 1 

board = [[1 for j in range(a)] for i in range(b)] # 그리드 만들기

k = 0 
l = 0
lst.sort()
for decision in lst :
    if decision[0] == 0 :
        for i in range(a) :
            board[decision[1]+k][i] = 0 
        k += 1 
    else :
        for i in range(b) :
            board[i][decision[1]+l] = 0
        l+=1

i,j = 0,0
while board[i][j] ==0 :
    pass