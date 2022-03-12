import sys 

sys.stdin = open('input.txt','r')

def dfs(x,arr) :
    #tmp는 연산합
    global tmp
    #ans는 최소값
    global ans

    # #끝까지 다 돌면
    # if tmp > ans:
    #     return

    if x == N :
        #최소값을 갱신한다.
        ans = min(ans,tmp)
        return

    #행고정 열을 돌면서
    for i in range(N):
        #방문하지 않았으면
        if not(i in arr) :

            #해당 값을 연산에 추가
            tmp += grid[x][i]
            #연산 결과가 연산 최소값보다 크면 break
            if tmp > ans:
                tmp -= grid[x][i]
                continue

            #방문표시하고
            arr.append(i)
            #연산 결과가 연산 최소값보다 작으면 다음 행을 탐색
            dfs(x+1,arr)
            #탐색 끝나면 연산값을 빼주고
            tmp -= grid[x][i]
            #방문표시 취소..
            arr.pop()


T = int(input())

for t in range(1,T+1) :
    N = int(input())
    tmp = 0
    grid = [list(map(int,input().split())) for _ in range(N)]
    arr = []
    ans = 1e9
    dfs(0,arr)
    print(f'#{t} {ans}')