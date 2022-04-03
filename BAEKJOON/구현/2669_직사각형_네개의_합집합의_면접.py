import pprint
board = [[0 for j in range(100)] for i in range(100)] # 100 x 100 그리드 만들기 
for _ in range(4) : #4개의 직사각형을 돌며 
    a, b, c, d = map(int, input().split()) #각 좌표를 a,b,c,d에 저장 
    for i in range(a, c) : #i가 직사각형 면적 안에 있게 하기 위해 for문을 돌린다.
        for j in range(b, d) : #y좌표를 돌며 값을 입력시킨다.
            if board[i][j] == 1 : #만약 값이 입력되어 있으면 
                continue          #continue
            else :
                board[i][j] = 1 #아니면 값을 입력한다. (직사각형이 겹치지 않게 하기 위해서 )

ans = 0
for i in range(100): #좌표를 돌며 최종적으로 값이 입력되어있으면 더한다. 
    for j in range(100):
        if board[i][j] == 1 :
            ans += 1
print(ans)