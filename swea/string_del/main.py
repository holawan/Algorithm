T = int(input())
for t in range(1, T + 1):
    lst = [] #빈리스트 만들기
    S = input()
    for s in S: #입력된 문자열을 순회하며
        if lst == []: #빈 문자열이면
            lst.append(s) #s 넣기
        elif s == lst[-1]: #현재 문자가 리스트의 마지막과 같으면
            lst.pop(-1) #중복이므로 제거
        else:
            lst.append(s) #아니면 추가
    print(f'#{t} {len(lst)}')
