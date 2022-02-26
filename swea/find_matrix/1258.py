## 용기는 n x n 배열
#빈 용기 = 0, 화학물질이 들어있으면 종류에 따라 1~9 
#조건 1 화학물질이 담긴 용기들이 사각형을 이루고 있으며, 내부에 빈 용기 없음 (행렬 안에 0이 없음 )
#조건 2 반드시 가로와 세로가 다름 
#조건 3 행렬과 행렬 사이에는 빈 용기 (0xn or nxo 행렬)이 있다. (대각선은 있을수도 없을수도)
# 출력 형식은 n*m이 작은 순서대로, 같을 경우에는 행(n)이 작은 순으로 출력 

# import sys

# sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,2+1) :
    n = int(input())

    grid = [list(map(int,input().split())) for _ in range(n)]
    #결과를 담을 리스트
    res = []

    #행렬을 돌며
    for r in range(n) :
        for c in range(n) :
            #값이 있으면 x,y의 초기값으로 설정 
            if grid[r][c] :
                x = r
                y = c 
            
            #행의 길이, r의 길이 초기값
                len_r = 0
                len_c = 0
            #열을 순회하며 범위 내면서, 값이 있으면 y를 증가시킴 
                while 0<=y<n and grid[x][y] :
                    y += 1
            #열 최대값 저장
                len_c = y-1 
            #행을 순회하며 범위 내면서, 값이 있으면 x를 증가시킴
                while 0<=x<n and grid[x][len_c] :
                    x += 1 
                len_r = x-1 

            #지나온 값은 0으로 변경
                for k in range(r,x) :
                    for m in range(c,y) :
                        grid[k][m] = 0 
            #결과에 저장
                res.append((len_r-r+1,len_c-c+1))

    print(res)
    matrix = []
    for r,c in res :
        matrix.append([r*c,r,c])
    matrix.sort()
            

    #행렬의 개수 출력 
    print(f'#{t} {len(matrix)}',end=' ')
    #크기가 낮은 순으로 출력 
    for i in matrix :
        print(i[1],i[2],end=' ')
    print()
