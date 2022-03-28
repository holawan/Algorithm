def runs(lst) :
    #중복 숫자가 있을 수 있으므로 임시적으로 set으로 중복제거 
    lst = list(set(lst))
    n = len(lst)
    if n<3 :
        return 0
    #정렬하고 
    lst.sort()
    x = 0
    #세자리수가 연속되면 1 리턴 
    while x<n-2:
        if lst[x+1]-lst[x] == 1 and lst[x+2]-lst[x+1] == 1 :
            return 1 
        else :
            x += 1 
    return 0 

def triple(lst) :
    n = len(lst) 
    if n<3 :
        return 0
    x = 0
    #정렬하고 
    lst.sort()
    #세개 숫자가 연속이면 1리턴 
    while x<n-2:
        if lst[x]==lst[x+1] and lst[x+1] == lst[x+2] :
            return 1 
        else :
            x += 1 
    return 0 

def play(lst) :
    p1 = []
    p2 = []
    for i in range(0,len(lst),2) :
        p1.append(lst[i])
        if runs(p1) or triple(p1) :
            return 1
        p2.append(lst[i+1])
        if runs(p2) or triple(p2) :
            return 2 
    return 0 

T = int(input())

for t in range(1,T+1) :
    lst = list(map(int,input().split()))
    ans = play(lst)
    print(f'#{t} {ans}')