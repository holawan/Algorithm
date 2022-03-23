import sys 

sys.stdin = open('input.txt','r')


T = int(input())

n,m = map(int,input().split())

grid = [list(map(int,input())) for _ in range(n)]

lst = []
codes = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]


for i in codes :
    print(len(i)) 