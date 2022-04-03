
T = int(input())
for t in range(T) :
    #전화번호수 
    n = int(input())
    lst = []

    #전화번호 넣어주기 
    for i in range(n) :
        x = input()
        lst.append(x)
    #정렬 
    lst.sort()
    #초기정답 yes
    res = 'YES'
    #내 전화번호가 다음전화번호의 접두어인지 확인 
    for i in range(n-1) :
        if lst[i] == lst[i+1][:len(lst[i])] :
            res = 'NO'
            print(res)
            break
    else :
        print(res)