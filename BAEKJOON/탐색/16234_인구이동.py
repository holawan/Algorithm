from collections import deque

#절대값 T/F 
def func(x,y) :
    if L<=abs(x-y)<=R :
        return True
    else :
        return False

def bfs(r,c,visited) :
    #최종 인구 합 
    res = grid[r][c]
    #큐 만들기 
    q = deque([(r,c)])
    #인접 국가 리스트 
    div_city = [(r,c)] 
    
    #방문표시 
    visited[r][c] = 1
    while q :
        cr,cc = q.popleft()
        #네방향을 돌면서 방문하지 않았고, 절대값 조건에 만족하면 큐에 넣고, 인접 국가 리스트에도 넣고 국가의 합에도 추가 
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<=nr<N and 0<=nc<N and func(grid[cr][cc],grid[nr][nc]) and not visited[nr][nc] :
                visited[nr][nc] = 1 
                q.append((nr,nc))
                res += grid[nr][nc]
                div_city.append((nr,nc))
    #인접국가 길이와, 국가 합, 인접국가 리스트 리턴 
    return len(div_city),res,div_city

def func2(N) :
    #날짜를 표시할 cnt 
    global cnt 
    while True :
        #방문배열 
        visited = [[0]*N for _ in range(N)]
        #추후 인구를 재정렬할 리스트 
        lst = []
        #그리드를 돌면서 
        for r in range(N) :
            for c in range(N) :
                #bfs를 돌고 길이,인구합,인접국가리스트 리턴 
                l,res,d = bfs(r,c,visited)
                #길이가 1보다 크면 재정렬 리스트에 포함 
                if l > 1 :
                    lst.append((res,d))
        #재정렬 리스트가 비어있으면 더이상 움직일 수 없으니까 끝내기 
        if lst == [] :
            return 
        #재정렬 리스트가 있으면 재정렬 리스트를 돌면서 인구 재조정 
        for i in range(len(lst)) :
            #d = 인구 합 // 국가수 
            d = lst[i][0]//len(lst[i][1])
            for r,c in lst[i][1] :
                grid[r][c] = d
        #while문 끝날때마다 날짜 하루씩 추가 
        cnt += 1 

N,L,R = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

cnt = 0

func2(N)
print(cnt)