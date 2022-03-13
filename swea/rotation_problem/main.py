import sys 

sys.stdin = open('input.txt','r')



def rotation(arr) :
    #반복횟수와, 리스트 
    global cnt,lst
    #반복이 10번이면 
    if cnt == m :
        #리스트를 arr로 저장하고 return
        lst = arr 
        return 
    #리스트는 index1부터 끝까지 더한 값에서 첫번째 값을 더함 
    arr = arr[1:]+[arr[0]]
    #반복횟수 추가 
    cnt += 1
    
    rotation(arr)


T = int(input())

for t in range(1,T+1) : 
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    cnt = 0
    rotation(lst)
    print(f'#{t} {lst[0]}')

