#스킵 함수 : 뛰어넘을 간격을 결정
def skip(p,last) :
    #last = t[i+m-1]
    #탐색한 텍스트 마지막 글자가(i+m-1) 패턴내에 있는지 확인한다.
    for idx in range(m-2,-1,-1) :
        #패턴을 뒤에서부터 돌면서
        if p[idx] == last : #마지막 글자와 패턴에 일치하는 값이 있으면
            return m-idx-1 #길이-i-1 만큼 리턴(스킵할 정도)
    return len(p) #마지막 글자와 패턴에 일치하는 값이 없으면 패턴의 길이만큼 스킵

def boyer(p,t) :
    cnt = i = 0
    #텍스트-패턴 길이까지
    while i<= n-m :

        for j in range(m-1,-1,-1) :
            if p[j] != t[i+j] :
                jump = skip(p,t[i + m -1])
                break

        if j == 0 :
            return 1
        else :
            i += jump

    return 0

T = int(input())
for ts in range(1,T+1) :
    p = input()
    t = input()
    #두 문자열의 길이 받아오기
    m  = len(p) #패턴
    n = len(t) #텍스트
    print(f'#{ts} {boyer(p,t)}')