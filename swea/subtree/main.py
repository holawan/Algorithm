import sys 

sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1) : 
    #
    E,root = map(int,input().split())

    # parent = [[_] for _ in range(E+1)]
    
    #자식노드 리스트 만들기
    c1 = [0]*(E+2)
    c2 = [0]*(E+2)

    #부모자식 쌍 받아오기
    lst = list(map(int,input().split()))
    
    #첫째 자식 비어있으면 거기 넣고 아니면 둘째에 넣음 
    for i in range(0,E*2,2) :
        a,b = lst[i],lst[i+1]

        if c1[a] == 0 :
            c1[a] = b 
        else :
            c2[a] = b 

    #연결 수 나를 포함해야해서 1부터 시작 
    cnt = 1
    def find(c1,c2,root) :
        global cnt 
        #연결되어 있으면 1더하고 해당 노드에서 탐색 
        if c1[root] :
            cnt += 1 
            find(c1,c2,c1[root])
        if c2[root] :
            cnt += 1 
            find(c1,c2,c2[root])
    find(c1,c2,root)
    print(f'#{t} {cnt}')