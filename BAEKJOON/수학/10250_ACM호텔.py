n = int(input())
for i in range(n) :

    #호텔의 층, 각층의 방, 손님 번호 
    H,W,N = map(int,input().split())

    lst = list([0]*W for i in range(H))
    
    #손님이 만날때까지 반복문 돌기 
    n = 0
    for i in range(1,W+1) :
        for j in range(1,H+1) :
            n += 1
            if n == N :
                print(j*100 + i)
                break
