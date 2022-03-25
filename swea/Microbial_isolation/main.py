from pprint import pprint
import sys 
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1) : 
    #셀의 수, 격리시간, 미생물 수 
    N,M,K = map(int,input().split())
    lst = []
    for _ in range(K) :
        lst.append(list(map(int,input().split())))

    dr = [0,-1,1,0,0]
    dc = [0,0,0,-1,1]

    for m in range(M) :
        for l in lst :
            l[0] = l[0] + dr[l[3]]
            l[1] = l[1] + dc[l[3]]
            if l[0] == 0 or l[0] == N-1 or l[1] == 0 or l[1] == N-1 :
                l[2] //= 2 
                if l[3] % 2 :
                    l[3] += 1 
                else :
                    l[3] -= 1 

        lst.sort(key = lambda x:(x[0],x[1],x[2]),reverse = True)

        i = 1
        while i<len(lst) :
            if lst[i-1][:2] == lst[i][:2] :
                lst[i-1][2] += lst[i][2] 
                lst.pop(i)
                i-=1
            i += 1 
        
    ans = 0
    for i in lst :
        ans += i[2]
    print(f'#{t} {ans}')

            