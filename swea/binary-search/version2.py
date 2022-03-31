def binary_search(lst,target,l,r) :
    before = -1
    while l<=r :
        m = (l+r)//2
        if lst[m] == target :
            return True
        #타겟이 리스트의 왼쪽에 있으면 
        elif lst[m]>target :
            r = m-1
            now = 0
            if now == before :
                return False 
            else :
                before = now 
        #타겟이 리스트 오른쪽에 있으면 
        elif lst[m]<target :
            l = m+1
            now = 1 
            if now == before :
                return False 
            else :
                before = now 
    return 0


T = int(input())

for t in range(1,T+1) : 
    N1,N2 = map(int,input().split())
    lst1 = list(map(int,input().split()))
    lst1.sort()
    lst2 = list(map(int,input().split()))

    cnt = 0
    for x in lst2 :
        if binary_search(lst1,x,0,N1-1) :
            cnt += 1 
    print(f'#{t} {cnt}')


