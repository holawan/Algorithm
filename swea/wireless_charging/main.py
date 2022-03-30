import sys 
sys.stdin = open('input.txt', 'r')

from collections import deque
dx = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))
 
 
def check_bcs():
    for i in range(1, A + 1):
        r, c, C, p = BCs[i]

        visited = [[0] * 11 for _ in range(11)]
        que = deque()

        #방문처리 
        visited[r][c] = 1
        #배터리 위치 큐에 넣고 
        que.append((r, c, 0))

        while que:
            cr, cc, cl = que.popleft()
            #일치하는 그리드에 배터리 번호 추가 
            grid[cr][cc].append(i)

            #최대 범위에 도달하면 큐에 그만넣고 계속 집어넣기 
            if cl == C:
                continue
            #아니면 상하좌우 돌면서 큐에 추가 
            for d in dx[1:]:
                nr, nc = cr + d[0], cc + d[1]
                if not (1 <= nr <= 10) or not (1 <= nc <= 10) or visited[nr][nc]:
                    continue
 
                visited[nr][nc] = True
                que.append((nr, nc, cl + 1))
 

 
def get_result(a_bcs, b_bcs):
    result = 0
    #a가 비어있으면 b만 배터리 충전 
    if not a_bcs:
        for c in b_bcs:
            result = max(BCs[c][3], result)
    #b가 비어있으면 a만 배터리 충전 
    elif not b_bcs:
        for c in a_bcs:
            result = max(BCs[c][3], result)
    #둘다 있을 때 
    else:
        #a돌고 
        for ac in a_bcs:
            #b 돌면서 
            for bc in b_bcs:

                #둘이 위치가 같으면 반절씩 나눠서 가지기 
                if ac == bc:
                    result = max(BCs[ac][3], result)
                #둘이 위치가 다르면 각자의 위치에 배터리로 충전하기 
                else:
                    result = max(BCs[ac][3] + BCs[bc][3], result)
    return result
 
 
def move():
    ar, ac = 1, 1
    br, bc = 10, 10
    result = 0
    for m in range(M):
        #처음위치부터  
        a_bcs = grid[ar][ac][:]
        b_bcs = grid[br][bc][:]
        #결과에 충전량 추가 
        result += get_result(a_bcs, b_bcs)
        #이동거리 
        ad = dx[p1[m]]
        bd = dx[p2[m]]
        #이동시키기 
        ar, ac = ar + ad[0], ac + ad[1]
        br, bc = br + bd[0], bc + bd[1]
    #리스트 정렬 
    a_bcs = grid[ar][ac][:]
    b_bcs = grid[br][bc][:]
    result += get_result(a_bcs, b_bcs)
    return result
 
T = int(input())
for t in range(1, T+1):
    #이동시간, 배터리 개수 
    M, A = map(int, input().split())
    #A,B의 이동 가져오기 
    p1 =list(map(int, input().split()))
    p2 =list(map(int, input().split()))
    #배터리 정보 
    BCs = [None]
    for x, y, C, p in [tuple(map(int, input().split())) for _ in range(A)]:
        BCs.append((y, x, C, p))

    grid = [[[] for _ in range(11)] for _ in range(11)]
    check_bcs()
    ans = move()
    print(f'#{t} {ans}')