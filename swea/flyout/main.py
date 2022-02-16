import sys
sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1) :
    n, m = map(int,input().split())

    grid = [list(map(int,input().split())) for _ in range(n)]

    result = []
    for row in range(n-m+1) : #행을 n-m+1 범위로 순회
        for column in range(n-m+1): #행고정 후 열 n-m+1 범위로 순회
            my_sum = 0 #배열의 합
            for i in range(m) : #m만큼 행을 순회하며 각 행마다 m개의 열을 더한다
                my_sum += sum(grid[row+i][column:column+m])
            result.append(my_sum) #결과 리스트에 추가


    print(f'#{t} {max(result)}')
