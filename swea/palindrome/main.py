T = int(input())

def func(n,m,grid) :
    for row in range(n) : #행을 순회
        for column in range(n-m+1) : #열을 n-m+1 만큼 (주어진 회문의 길이만큼 돌며)
            if grid[row][column : column + m] == grid[row][column:column + m][::-1] : #회문이면
                return ''.join(grid[row][column : column + m]) #반환
                # exit()

    grid2 = list(map(list,zip(*grid))) #행렬전환

    for row in range(n) :
        for column in range(n-m+1) :
            if grid2[row][column : column + m] == grid2[row][column:column + m][::-1] :
                return ''.join(grid2[row][column : column + m])

for t in range(1,T+1) :
    n,m = map(int,input().split())#행, 회문 길이

    grid = [list(input()) for _ in range(n)]

    print(f'#{t} {func(n,m,grid)}')