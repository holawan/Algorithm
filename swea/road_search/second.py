import sys 

sys.stdin = open('input.txt','r')

#dfs알고리즘 
def dfs(x) :
    #해당 도시에 방문표시
    visited[x] = 1 
    #다른 도시들을 탐색하며 
    for i in range(1,100) :
        #가는 루트가 있으며 아직 안갔으면 
        if grid[x][i] == 1 and not visited[i] :
            #방문표시하고 
            visited[i] = 1
            #그 도시를 시작으로 dfs  
            dfs(i)


for tc in range(1,11) :
    t,n = map(int,input().split())
    
    #이동경로 받기 
    nodes = list(map(int,input().split()))
    
    #이동 가능 표시 그리드 
    grid = [[0]*100 for _ in range(100)]
    
    #이동가능 경로에 1로 표시 
    for i in range(0,2*n,2) :
        a,b = nodes[i],nodes[i+1] 
        grid[a][b] = 1
    
    
    #방문표시 리스트
    visited = [0]*100

    dfs(0) 

    if visited[99] == 1 :
        print(f'#{t} 1')
    else :
        print(f'#{t} 0')

