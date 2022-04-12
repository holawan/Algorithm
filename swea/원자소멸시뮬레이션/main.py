import sys 
sys.stdin = open('input.txt','r')

dr = [0, 0, -0.5, 0.5]
dc = [0.5, -0.5, 0, 0]

T = int(input())
for t in range(1,T+1) :
    N = int(input())
    #원자 받아오기 
    lst = [list(map(int,input().split())) for _ in range(N)]
    #초기 에너지
    energy = 0

    #리스트에 원소가 있다면 
    while lst :
        #초기 인덱스 
        cnt = 0 
        p_lst1 = []
        for l in lst :
            #원자 움직이기 
            l[0] = l[0]+dr[l[2]]
            l[1] = l[1]+dc[l[2]]
            #원자가 최고 위치까지 갔는데, 터지지 않았으면 리스트에서 제거하기 
            if l[0]>1000 or l[0]<-1000 or l[1]>1000 or l[1]<-1000 :
                p_lst1.append(cnt)
            cnt += 1 
        
        p_lst1.sort(reverse=True)
        for p in p_lst1:
            lst.pop(p)
        #x,y좌표로 정렬하기 
        lst.sort(key = lambda x:(x[0],x[1]))
        #위치 비교 초기값 
        i = 1 
        #pop할 리스트 
        p_lst = set()
        while i < len(lst) :
            #앞뒤가 같으면 p_lst에 넣기 
            if lst[i-1][:2] == lst[i][:2] :
                p_lst.add(i-1)
                p_lst.add(i)
            i+= 1 
        #set으로 중복 제거하고 리스트를 큰 순서대로 정렬 
        p_lst = sorted(list(p_lst),reverse=True)
        #값이 있다면 리스트를 돌면서 에너지에 추가해주고 삭제하기
        
        if p_lst :
            for p in p_lst :
                energy += lst[p][3]
                lst.pop(p)

    print(f'#{t} {energy}')