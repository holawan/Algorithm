import sys

sys.stdin = open('input.txt','r')

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for tc in range(10):
    n = int(input())
    arr = [[0]+list(map(int,input().split()))+[0] for _ in range(100)]
    for j in range(102):
        if arr[99][j] == 2: # 2일 때 출발
            x = 99
            y = j

            # 경우의 수 3가지 아래-> 왼 or 오 / 왼-> 아래 / 오->아래
            # 문제는 왼쪽으로 이동했을 시 오른쪽은 탐색하면 안됨. 오른쪽도 마찬가지.
            # 지나간 건 0으로 바꿔주기!
            while x != 0:
                # 방향에 맞게 한칸씩 이동

                # 아래
                if arr[x][y+1] == 0 and arr[x][y-1] == 0:
                    arr[x][y] = 0
                    d = 3
                    x = x + dx[d]
                    y = y + dy[d]

                # 우
                elif arr[x][y+1] == 1:
                    arr[x][y] = 0
                    d = 0
                    x = x + dx[d]
                    y = y + dy[d]

                # 좌
                elif arr[x][y-1] == 1:
                    d = 2
                    x = x + dx[d]
                    y = y + dy[d]

            print(j)