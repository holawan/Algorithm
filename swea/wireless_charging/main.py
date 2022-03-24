from pprint import pprint
import sys 

sys.stdin = open('input.txt','r')

T = int(input())

#이동시간과 충전기
M,A = map(int,input().split())

#유저별 이동(1,1/10,10)
usera = list(map(int,input().split()))
userb = list(map(int,input().split()))

#충전기 리스트들 
aplst = []
for i in range(A) :
    aplst.append(list(map(int,input().split())))
aplst.sort(key=lambda x:x[3])

grid = [[0]*11 for _ in range(11)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]
for ap in aplst :
    #좌표 중심값은 충전량
    #충전범위 
    ranges = ap[2]

    r,c = ap[1],ap[0]
    #충전범위 가장 위에서 중심으로 오면서 
    k = 0
    tmp = []
    for i in range(ranges+1) : 
        tmp.append([i for i in range(c-k,c+k+1)])
        k += 1 
    accept = []
    for i in range(ranges+1) :
        for j in tmp[-i-1] :
            if 1<=i+r<11 and 1<=j<11 :
                if grid[r+i][j] :
                    accept.append([r+i,j,grid[r+i][j],ap[3]])
                    grid[r+i][j] = -1
                else :
                    grid[r+i][j] = ap[3]
                
            if 1<=r-i<11 and 1<=j<11 :
                if i!=0 and grid[r-i][j] :
                    accept.append([r-i,j,grid[r-i][j],ap[3]])
                    grid[r-i][j] = -1
                else :
                    grid[r-i][j] = ap[3]

ai,aj = 1,1 
bi,bj = 10,10
dr = [0,-1,0,1,0]
dc = [0,0,1,0,-1]

suma = grid[ai][aj]
sumb = grid[bi][bj]
lst1,lst2 = [],[]
for i in usera :
    ai,aj = ai+dr[i],aj+dc[i]
    suma += grid[ai][aj]
    lst1.append(grid[ai][aj])
for i in userb :
    bi,bj = bi+dr[i],bj+dc[i]
    sumb += grid[bi][bj]
    lst2.append(grid[bi][bj])

print(lst1)
print(lst2)
print(suma+sumb)