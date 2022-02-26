## 용기는 n x n 배열
#빈 용기 = 0, 화학물질이 들어있으면 종류에 따라 1~9 
#조건 1 화학물질이 담긴 용기들이 사각형을 이루고 있으며, 내부에 빈 용기 없음 (행렬 안에 0이 없음 )
#조건 2 반드시 가로와 세로가 다름 
#조건 3 행렬과 행렬 사이에는 빈 용기 (0xn or nxo 행렬)이 있다. (대각선은 있을수도 없을수도)
# 출력 형식은 n*m이 작은 순서대로, 같을 경우에는 행(n)이 작은 순으로 출력 

# import sys

# sys.stdin = open('input.txt','r')

T = int(input())
# for t in range(1,T+1) :
n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

res = []

for r in range(n) :
    for c in range(n) :
        if grid[r][c] :
            x = r
            y = c 
            
            max_r = 0
            max_c = 0

            while 0<=y<n and grid[x][y] :
                y += 1
            max_c = y-1 

            while 0<=x<n and grid[x][max_c] :
                x += 1 
            max_r = x-1 

            for k in range(r,x) :
                for m in range(c,y) :
                    grid[k][m] = 0 
            res.append((max_r-r+1,max_c-c+1))
            for i in grid :
                print(i)
            print('------------------------')
print(res)
# matrix = []
# for r,c in res :
#     matrix.append([r*c,r,c])
# matrix.sort()
# print(matrix)            

# print(f'#{T} {len(matrix)}',end='')
# for i in range(len(matrix)) :
#     print(matrix[i][1],matrix[i][2],end='')
# print()
