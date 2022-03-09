T  = int(input())
for t in range(1,T+1) : 
    n = int(input()) #노선
    #1 = 일반, #2 = 급행 #3 = 광역급행
    #정류장은 1~1000 
    stop = [0]*1001

    for i in range(n) :
        type,start,end = map(int,input().split())
        stop[start]+=1 ;stop[end]+=1 
        for move in range(start+1,end) :
            if type == 1 :
                stop[move] +=1 
            elif type == 2 :
                if start%2 :
                    if move%2 :
                        stop[move] +=1
                else :
                    if move%2 == 0 :
                        stop[move] +=1 
            else :
                if start%2 :
                    if move%3 == 0 :
                        if move%10 == 0 :
                            continue
                        else :
                            stop[move] +=1 
                else :
                    if move%4 == 0:
                        stop[move] +=1 
    print(f'#{t} {max(stop)}')
    print(stop[:20])


