import copy 

N,M = map(int,input().split())

grid = []
cctv = []

case = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(depth,now_grid):
    global res 
    if depth==len(cctv) :
        cnt = 0 
        for i in range(N) :
            cnt += now_grid[i].count(0)
        res = min(res,cnt)
        return 
    tmp_grid = copy.deepcopy(now_grid)
    cctv_num,tmp_r,tmp_c = cctv[depth]
    for i in case[cctv_num] :
        fill(tmp_grid,i,tmp_r,tmp_c)
        dfs(depth+1,tmp_grid)
        tmp_grid = copy.deepcopy(now_grid)

def fill(now_grid2,idx,tmp_r,tmp_c) :
    for d in idx :
        nr,nc = tmp_r,tmp_c 
        while True :
            nr += dr[d]
            nc += dc[d]
            if not 0 <= nr < N or not 0 <= nc < M :
                break
            if now_grid2[nr][nc] == 6 :
                break
            elif now_grid2[nr][nc] == 0 :
                now_grid2[nr][nc] = 7


for r in range(N) :
    tmp = list(map(int,input().split()))
    grid.append(tmp)
    for c in range(M) :
        if tmp[c] in [1,2,3,4,5] : 
            cctv.append([tmp[c],r,c])
res = 1e9



dfs(0,grid)
print(res)