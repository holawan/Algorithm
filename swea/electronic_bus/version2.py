T = int(input()) #테스트 케이스

def func(x,cnt) : 
    global res
    
    #충전횟수가 최소값보다 크면 리턴 
    if cnt >= res :
        return

    #현재 위치가 종착지보다 크거나 같으면 리턴 
    if x >=  data[0] :
        res = min(res,cnt)
        return

    for i in range(1,data[x]+1) :
        #이동거리 + , 이동가능거리는 현재에서 충전으로 움직일 수 있는만큼 움직이고 i 뺌 
        func(x+i,cnt+1)

for t in range(1,T+1): #출력형식 맞추기 위해 1부터 T+1 까지
    data = list(map(int,input().split()))
    res = 101
    #출발지점, 교환횟수  
    func(1,-1)
    print(f'#{t} {res}')