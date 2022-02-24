T = int(input())
for t in range(1,T+1) :
    #압축된 문자 받기 
    n = int(input())
    #압축해제를 위한 리스트
    lst = []
    #문자를 돌며 extend를 이용해 문자를 압축 개수만큼 추가
    for _ in range(n) :
        a,b = input().split()
        lst.extend(a*int(b))
    #문자열로 변경
    s = ''
    for i in lst :
        s+= i
    print(f'#{t}')
    #10줄 간격으로 출력 
    for i in range(0,len(s),10) :
        print(s[i:i+10])
