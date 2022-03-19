import sys 

sys.stdin = open('input.txt','r')

def DFS(x,sum) :
    global sol

    if x>= n :
        if sum == k :
            sol +=1 
        return
    
    DFS(n+1,sum+lst[x]) #숫자를 포함하는 경우 
    DFS(n+1,sum) #숫자를 포함하지 않는 경우


T = int(input())

for t in range(1,T+1) :
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    sol = 0
    DFS(0,0)
    print(f'#{t} {sol}')