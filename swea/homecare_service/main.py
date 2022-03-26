import sys 
from collections import deque 
sys.stdin = open('input.txt','r')


T = int(input())
N,M = map(int,input().split())
dr = [1,0,-1,0]
dc = [0,-1,0,1]
grid = [list(map(int,input().split())) for _ in range(N)]
def bfs(si,sj,visited) : 
    que = deque()
    que.append([si,sj])
    visited.append([si,sj])
    while que :
        i,j = que.popleft()
        for d in range(4) :
            ni = i+dr[d]
            nj = j+dr[d]
            if 0<=ni<N and 0<=nj<N and not [ni,nj] in visited :
                que.append([ni,nj]) 

for i in range(N) :
    for j in range(N) :
        bfs(i,j,[])
