from collections import deque 
n,m = map(int,input().split())

#그리드 받아오기 
grid = [list(map(int,input().split())) for _ in range(n)]
#방향 설정 
dr = [0,-1,0,1]
dc = [1,0,-1,0]

#큐 만들기 
q = deque()
#남은 치즈는 remain
remain = 0
#방문배열 
visited =[]

#배열을 돌면서 
for r in range(n) :
    for c in range(m) :
        #가장자리를 큐에 넣는다. 그리고 방문처리한다. 
        if r == 0 or c == 0 or r == n-1 or c == m-1 :
            q.append([r,c])
            visited.append((r,c))
        #치즈가 잇으면 remain에 추가해준다. 
        elif grid[r][c] == 1 :
            remain += 1
#공기에 담은 치즈를 담을 배열 
rm = []
#반복횟수 
cnt = 0
while True :
    cnt +=1
    #공기에 닿은 치즈들이 담겨있으면 치즈를 큐로 사용  
    if rm :
        tmp_q = deque(rm[:])
    #아니면 가장자리를 큐로 사용 
    else :
        tmp_q = q
    rm = []
    
    tmp = 0
    #큐에 값이 있으면 
    while tmp_q :
        # 큐에서 원소를 꺼내서 
        cr,cc = tmp_q.popleft()
        # 4방향을 순회한다. 
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d] 
            #순회한 방향이 범위 안에 잇으면서 방문하지 않았을 때 
            if 0<nr<n-1 and 0<nc<m-1 and not (nr,nc) in visited :
                #1이면 공기에 닿았다고 판단한다. 
                #공기에 닿은 부분만 제거할것이기 때문에 큐에는 넣지 않는다.
                if grid[nr][nc] == 1 :
                    rm.append([nr,nc])
                    #공기에 닿으면 공기가 되므로 0으로 바꾼다. 
                    grid[nr][nc] = 0
                    #공기에 닿은 치즈 수 
                    tmp +=1 
                #그냥 공기면 큐에 넣어줘서 계속 탐색하게 한다. 
                elif grid[nr][nc] == 0 :
                    tmp_q.append([nr,nc])
                #다시 방문하지 않도록 방문처리한다. 
                visited.append((nr,nc)) 
    #남은 치즈에서 공기에 닿은 치즈를 빼준다. 
    remain = remain-tmp
    #남은 치즈가 없으면 종료한다. 
    if remain == 0 :
        break

#반복횟수 
print(cnt)
#마지막 남았던 치즈 수 
print(tmp)