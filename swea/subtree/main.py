import sys 

sys.stdin = open('input.txt','r')

T = int(input())

E,root = map(int,input().split())

# parent = [[_] for _ in range(E+1)]

c1 = [0]*(1001)
c2 = [0]*(1001)
lst = list(map(int,input().split()))
for i in range(0,E*2,2) :
    a,b = lst[i],lst[i+1]

    if c1[a] == 0 :
        c1[a] = b 
    else :
        c2[a] = b 
cnt = 0
def find(root,c1,c2):
    