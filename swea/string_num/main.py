T = int(input())

def func(t, p):
    match = {} #str1에 있는 문자를 담을 딕셔너리
    for Str in p: #중복이면 제거하고 아니면 해당 문자를 key로 딕셔너리 생성
        match[Str] = 0
    i = 0
    j = 0
    cnt = 0
    for i in range(n): #텍스트 순회
        for j in match.keys(): #패턴 순회하며
            if t[i] == j:
                match[j] += 1 #일치하면 패턴의 인덱스에 해당하는 문자를 딕셔너리 내에서 +=1
    return (max(match.values())) #딕셔너리 중 value가 가장 큰 값을 반환

for ts in range(1,T+1) :
    p = input() #패턴
    t = input() #텍스트
    m = len(p)
    n = len(t)


    print(f'#{ts} {func(t,p)}')



