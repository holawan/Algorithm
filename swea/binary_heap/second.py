def heap(x) :
    #루트 노드면 리턴
    if x == 1 :
        return
    #부모는 자식을 2로 나눈 몫 
    parents = x//2
    #자식이 크면 자리 바꾸고 
    if dic[x] < dic[parents] :
        dic[x],dic[parents] = dic[parents],dic[x]
        #재귀로 반복 정렬 
        heap(parents)


T = int(input())
for t in range(1,T+1) : 
    N = int(input())
    lst = list(map(int,input().split()))
    #딕셔너리 만들기
    dic = dict() 

    #1부터 돌면서
    for i in range(N) :
        #각 노드마다 번호 입력해주고 
        dic[i+1] = lst[i]
        print(dic)
        #힙으로 정렬 
        heap(i+1)
        print(f'sort :{dic}')

    ans = 0
    while N>1 :
        ans += dic[N//2]
        N //= 2 
    print(f'#{t} {ans}') 


